import requests
import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            value = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
        else:
            try:
                response = requests.get(
                    "https://api.coindesk.com/v1/bpi/currentprice.json"
                )
                j_son = response.json()
                usd = value * float(j_son["bpi"]["USD"]["rate_float"])
                print(f"${usd:,.4f}")
            except requests.RequestException:
                print("Bad request")


if __name__ == "__main__":
    main()
