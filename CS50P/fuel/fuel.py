def fraction():
    while True:
        try:
            x, y = input("Enter the fraction X/Y: ").split('/')
            int_x = int(x)
            int_y = int(y)
        except ValueError:
            print('X or Y is not an integer')
        else:
            try:
                if int_x > int_y and int_y != 0:
                    print('X is greater than Y')
                else:
                    return int_x/int_y
            except ZeroDivisionError:
                print('Y is 0')


def main():
    value = round(fraction() * 100)
    if value >= 99:
        print('F')
    elif value <= 1:
        print('E')
    else:
        print(f" { value }%")



if __name__ == "__main__":
    main()