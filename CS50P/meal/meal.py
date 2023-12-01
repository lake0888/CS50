def main():
    time = input('Enter the time ')
    time = convert(time)

    if time >= 7.0 and time <= 8.0:
        print('breakfast time ')
    elif time >= 12.0 and time <= 13.0:
        print('lunch time ')
    elif time >= 18.0 and time <= 19.0:
        print('dinner time ')


def convert(time):
    h, m = time.split(":")
    return int(h) + float(int(m)/60)


if __name__ == "__main__":
    main()