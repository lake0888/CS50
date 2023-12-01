# TODO

import sys


def get_Digits(number):
    cont = 0
    while int(number) != 0:
        cont += 1
        number = number / 10

    return cont


def main():
    number = input("Number: ")

    try:
        valNumber = int(number)
    except:
        valNumber = -1

    if valNumber != -1:
        s_fdigit = 0
        s_sdigit = 0
        flag = False

        cant_digits = get_Digits(valNumber)
        card = 0

        if cant_digits >= 13 and cant_digits <= 16:
            coeficent = pow(10, cant_digits - 2)
            card = int(valNumber / coeficent)

            while int(valNumber) != 0:
                # get last two digits
                rest = int(valNumber % 100)

                fdigit = int(rest % 10)
                sdigit = int(int(rest / 10) * 2)

                sdigit = int(sdigit % 10) + int(sdigit / 10)

                s_sdigit += sdigit
                s_fdigit += fdigit

                # set number
                valNumber = int(valNumber / 100)

            total = s_fdigit + s_sdigit
            flag = int(total % 10) == 0

        if flag == True:
            if int(card / 10) == 4:
                print("VISA")
            elif card == 34 or card == 37:
                print("AMEX")
            elif card >= 51 and card <= 55:
                print("MASTERCARD")
            else:
                flag = False

        if flag == False:
            print("INVALID")


if __name__ == "__main__":
    main()