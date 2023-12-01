def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    flag = True
    first_two = s[0:2]

    # check maximum of characters and first two characters
    if len(s) < 2 or len(s) > 6 or first_two.isdigit():
        flag = False

    # find the index of the first digit, checking from the position two
    index = -1
    i = 2
    while i < len(s) and flag and index == -1:
        current = s[i]
        if current.isdigit():
            index = i
        i += 1

    if flag and index != -1:
        sub_str = s[index:len(s)]
        if (len(sub_str) > 0 and sub_str[0] == '0') or sub_str.isdigit() == False:
            flag = False

    return flag

if __name__  == "__main__":
    main()