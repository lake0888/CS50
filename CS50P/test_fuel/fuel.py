def main():
    fraction = input()
    percentage = convert(fraction)
    try:
        value = gauge(percentage)
        print(value)
    except:
        print(percentage)


def convert(fraction):
    try:
        x, y = fraction.split("/")
        int_x = int(x)
        int_y = int(y)
        if int_x > int_y and int_y != 0:
            raise NameError("X is greater than Y")
        return str(round((int_x / int_y) * 100))
    except NameError as error:
        return error
    except ZeroDivisionError:
        return "Y cannot be 0"
    except ValueError:
        return "Invalid literal for a fraction"


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{ percentage }"


if __name__ == "__main__":
    main()
