def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    cost = 0
    while True:
        try:
            item = input('Item: ').title()
            cost += menu[item]
            float_value = "{:.2f}".format(cost)
            print("Total: $" + float_value)
        except EOFError:
            break
        except KeyError:
            print('Item no found')

if __name__ == "__main__":
    main()