def main():
    due = 50
    while due > 0:
        print(f"Amount Due: { due }")
        coin = input('Insert Coin: ')
        try:
            int_coin = int(coin)
            if int_coin == 25 or int_coin == 10 or int_coin == 5:
                due -= int_coin
        except:
            print('Invalid input')

    print(f"Change Owed: { due * -1 }")

if __name__ == "__main__":
    main()