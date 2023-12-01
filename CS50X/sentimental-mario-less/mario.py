# TODO

import sys

valHeight = -1


def check_height(height):
    flag = True
    try:
        valHeight = int(height)
    except:
        valHeight = -1

    if valHeight <= 0 or valHeight > 8:
        flag = False

    return flag


def main():
    flag = len(sys.argv) == 2

    if flag:
        height = sys.argv[1]
        flag = check_height(height)

    while flag == False:
        height = input("Height: ")
        flag = check_height(height)

    height = int(height)
    i = 1
    while i <= height:
        z = height - i
        j = 1
        while j <= height:
            if j <= z:
                print(" ", end="")
            else:
                print("#", end="")
            j += 1
        print("")
        i += 1


if __name__ == "__main__":
    main()