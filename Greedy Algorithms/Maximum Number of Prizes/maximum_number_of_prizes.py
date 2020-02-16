# python3
import math

def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    while n != 0:
        if n % 2 == 0 and n % 3 == 0:
            div = n // 2
        else:
            div = n // 2 + 1
        summands.append(div)
        n -= div

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
