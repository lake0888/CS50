def main():
    str = input("Greeting: ")
    print(value(str))

def value(greeting):
    if greeting == "Hello":
        return 100
    elif greeting == "What's up":
        return 0
    return 20


if __name__ == "__main__":
    main()