from random import randint


def get_Number(str):
    while True:
        try:
            number = int(input(str))
            if number <= 0:
                continue
        except ValueError:
            pass
        except EOFError:
            break
        else:
            return number


def main():
    level = get_Number("Level: ")
    number = randint(1, level)

    while True:
        guess = get_Number("Guess: ")
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            break

    print("Just right!")


if __name__ == "__main__":
    main()
