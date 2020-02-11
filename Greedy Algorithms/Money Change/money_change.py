# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    coins = [10, 5, 1]
    coins_list = []
    for coin in coins:
        num_of_coins, money = divmod(money, coin)
        coins_list.append(num_of_coins)
    return sum(coins_list)



if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
