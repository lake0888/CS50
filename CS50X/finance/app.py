from crypt import methods
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

from datetime import datetime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    purchase = db.execute(
        "SELECT symbol, SUM(shares) AS shares FROM operation WHERE user_id = ? GROUP BY symbol ORDER BY symbol ASC", session["user_id"])

    LIST = []

    total = 0
    for current in purchase:
        quote = lookup(current["symbol"])

        OPERATION = {}
        OPERATION["symbol"] = quote["symbol"]
        OPERATION["name"] = quote["name"]
        OPERATION["shares"] = current["shares"]
        OPERATION["price"] = usd(quote["price"])
        OPERATION["total"] = usd(quote["price"] * current["shares"])

        LIST.append(OPERATION)

        current_price = quote["price"]
        total += current_price * current["shares"]

    cash = db.execute("SELECT cash FROM users WHERE id = " + str(session["user_id"]))
    amount = usd(cash[0]["cash"])

    total += cash[0]["cash"]
    total_usd = usd(total)

    return render_template("index.html", purchase=LIST, cash=amount, total=total_usd)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        quote = lookup(symbol)
        cash = db.execute("SELECT cash FROM users WHERE id = " + str(session["user_id"]))

        if not symbol:
            return apology("must provide a symbol", 403)
        elif not shares or shares.isnumeric() == False:
            return apology("must provider an integer positive share")
        elif quote == None:
            return apology("symbol doesn't exist")
        elif cash[0]["cash"] < (int(shares) * quote["price"]):
            return apology("you cannot afford the number of shares at the current price")
        else:
            # INSERT NEW DATA
            db.execute("INSERT INTO operation(user_id, symbol, companyName, shares, price, date, type) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       session["user_id"], symbol, quote["name"], shares, quote["price"], time(), True)

            # UPDATE CASH OF USER
            amount = int(shares) * quote["price"]
            new_cash = cash[0]["cash"]
            new_cash -= amount
            db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, session["user_id"])

            flash("Bought!")

            return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    history = db.execute("SELECT * FROM operation WHERE user_id = " + str(session["user_id"]) + " ORDER BY id ASC")

    LIST = []

    for current in history:
        OPERATION = {}
        OPERATION["symbol"] = current["symbol"]
        OPERATION["name"] = current["companyName"]
        OPERATION["shares"] = current["shares"]
        OPERATION["price"] = usd(current["price"])
        OPERATION["date"] = current["date"]

        LIST.append(OPERATION)

    return render_template("history.html", list=LIST)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["name"] = rows[0]["username"].upper()

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("must provide a symbol")
        else:
            json_quote = lookup(symbol)
            if json_quote == None:
                return apology("Symbol " + symbol + " doesn't exist")

            text = "A share of " + json_quote["name"] + " (" + json_quote["symbol"] + ") costs " + usd(json_quote["price"])
            return render_template("/quoted.html", text=text)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was submitted
        if not username:
            return apology("must provide username")

        # Ensure password was submitted
        elif not password:
            return apology("must provide password")

        # Ensure password was submitted
        elif not confirmation:
            return apology("must provide confirmation password")

        # Ensure password are equal
        elif password != confirmation:
            return apology("the passwords do not match")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        if len(rows) != 0:
            return apology("The username already exists")
        else:
            last_id = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))
            # Remember which user has logged in
            session["user_id"] = last_id

            flash("Registered!")

            # Redirect user to home page
            return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("Symbol must provide", 403)
        elif not shares or shares.isnumeric() == False:
            return apology("Shares must provide an integer positive")
        else:
            c_shares = db.execute("SELECT SUM(shares) AS sum FROM operation WHERE user_id = ? AND symbol = ?",
                                  session["user_id"], symbol)
            print(c_shares)

            if int(shares) > c_shares[0]["sum"]:
                return apology("Too many shares")
            else:
                quote = lookup(symbol)
                # INSERT NEW DATA
                db.execute("INSERT INTO operation(user_id, symbol, companyName, shares, price, date, type) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           session["user_id"], symbol, quote["name"], int(shares) * -1, quote["price"], time(), False)

                cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

                quote = lookup(symbol)
                # UPDATE CASH OF USER
                amount = int(shares) * quote["price"]
                new_cash = cash[0]["cash"]
                new_cash += amount
                db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, session["user_id"])

                flash("Sold!")
                return redirect("/")

    else:
        purchase = db.execute("SELECT DISTINCT(symbol) FROM operation WHERE user_id = " + str(session["user_id"]))
        return render_template("sell.html", purchase=purchase)


def time():
    now = db.execute("SELECT DATETIME('now', 'localtime')")
    return now[0]["DATETIME('now', 'localtime')"]


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not password:
            return apology("must provide password", 403)
        elif not confirmation:
            return apology("must provide confirmation password", 403)
        elif password != confirmation:
            return apology("the passwords do not match")
        else:
            db.execute("UPDATE users SET hash = ?", generate_password_hash(password))
            flash("Password changed!")
            return redirect("/")
    else:
        return render_template("profile.html")