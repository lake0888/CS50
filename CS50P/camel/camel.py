def convertTo_snake_case(str):
    new_str = ""
    i = 0
    while i < len(str):
        current = str[i]
        if current.isupper():
            new_str += "_" + current.lower()
        else:
            new_str += current
        i += 1

    return new_str


def main():
    str = input('Enter the string ')
    str = convertTo_snake_case(str)
    print(str)


if __name__ == "__main__":
    main()