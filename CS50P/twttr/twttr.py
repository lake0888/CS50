def main():
    str = input('Input: ')
    print(f"Output: { shorten(str) } ")

def isvowel(char):
    return char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'

def shorten(str):
    new_str = ""
    i = 0
    while i < len(str):
        current = str[i]
        if isvowel(current.upper()) == False:
            new_str += current
        i += 1

    return new_str


if __name__ == "__main__":
    main()