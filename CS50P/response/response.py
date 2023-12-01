from validator_collection import checkers

def main():
    print(valid_email(input("What's your email address? ")))

def valid_email(email):
    return "Valid" if checkers.is_email(email) else "Invalid"



if __name__ == "__main__":
    main()