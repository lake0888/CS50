import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    flag = True
    if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        numbers = ip.split(".")
        for number in numbers:
            if not validate_number(int(number)):
                return False
    else:
        flag = False
    return flag


def validate_number(number):
    return number >= 0 and number <= 255


if __name__ == "__main__":
    main()