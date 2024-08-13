def main():
    price = 50
    coins = ['25', '10', '5']

    while price > 0:
        coin = input("Insert coin: ")
        if coin not in coins:
            print(f"Amount Due: {price}")
            return 1
        coin = int(coin)

        if price - coin <= 0:
            print(f"Change Owed: {coin - price}")
            return
        else:
            price = price - coin
            print(f"Amount Due: {price}")
    return


main()
