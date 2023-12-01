# TODO

import sys


def lenghtBy(text, type):
    i = 0
    count = 0
    flag = False
    while i < len(text):
        current = text[i].upper()
        if type == 0:
            flag = current >= 'A' and current <= 'Z'
        elif type == 1:
            flag = current == ' '
        else:
            flag = is_symbol(current)

        if flag:
            count += 1

        i += 1

    # ADD COUNT FOR LAST CHARACTER = ' '
    if type == 1:
        count += 1

    return count


def is_symbol(character):
    return (character == '!' or character == '.' or character == '?')


def show_result(index):
    if index < 0:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {round(index)}")


def main():
    text = input("Text: ")
    letters = lenghtBy(text, 0)
    words = lenghtBy(text, 1)
    sentences = lenghtBy(text, 2)

    L = (letters / words) * 100
    S = (sentences / words) * 100

    index = 0.0588 * L - 0.296 * S - 15.8
    show_result(index)


if __name__ == "__main__":
    main()