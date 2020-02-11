# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)
    weights_prices = [(w, p) for w, p in zip(weights, prices)]
    weights_prices.sort(key=lambda x: x[1] / x[0], reverse=True)
    total_price = 0
    for i in range(len(weights_prices)):
        if capacity == 0:
            return total_price
        a = min(weights_prices[i][0], capacity)
        total_price += a * weights_prices[i][1] / weights_prices[i][0]
        capacity -= a
    return total_price

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
