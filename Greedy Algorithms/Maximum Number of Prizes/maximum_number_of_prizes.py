# python3
import math

def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    l = 1
    while n > 0:
        if n <= 2 * l:
            summands.append(n)
            n -= n
            l += 1
        else:
            summands.append(l)
            n -= l
            l += 1



    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
