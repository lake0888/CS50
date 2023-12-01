# TODO

import sys

from cs50 import get_float


def _25(owed):
    return owed / 25


def _10(owed):
    return owed / 10


def _5(owed):
    return owed / 5


def _1(owed):
    return owed / 1


def main():
    flag = False
    while flag == False:
        owed = get_float("Change owed: ")
        if owed > 0:
            flag = True

    if flag == True:
        owed *= 100
        count = 0
        while owed > 0:
            if owed >= 25:
                _25(owed)
                owed -= 25
            elif owed >= 10:
                _10(owed)
                owed -= 10
            elif owed >= 5:
                _5(owed)
                owed -= 5
            else:
                _1(owed)
                owed -= 1
            count += 1

        print(count)


if __name__ == "__main__":
    main()