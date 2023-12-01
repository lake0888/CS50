def main():
    grocery = dict()

    while True:
        try:
            item = input().upper()
            if item not in grocery:
                grocery[item] = 1
            else:
                grocery[item] = grocery[item] + 1
        except EOFError:
            for x, y in sorted(grocery.items()):
                print(y, x)
            break


if __name__ == "__main__":
    main()