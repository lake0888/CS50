from random import randint


def main():
    level = get_level()

    i = 0
    score = 0
    while i < 10:
        try:
            x = generate_integer(level)
            y = generate_integer(level)
            z = x + y

            tries = 3
            while tries > 0:
                result = input(f" { x } + { y } = ")
                try:
                    if int(result) == z:
                        score += 1
                        break
                    elif int(result) != z:
                        raise ValueError
                except ValueError:
                    print("EEE")
                    tries -= 1

            if tries == 0:
                print(f" { x } + { y } = { z }")
        except EOFError:
            print("\n")
            break
        i += 1
    print(f"Score: { score }")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level != 1 and level != 2 and level != 3:
                continue
        except ValueError:
            pass
        except EOFError:
            print("\n")
            break
        else:
            return level


def generate_integer(level):
    _min = pow(10, level - 1)
    _max = pow(10, level) - 1
    if level == 1:
        _min = 0
    return randint(_min, _max)


if __name__ == "__main__":
    main()
