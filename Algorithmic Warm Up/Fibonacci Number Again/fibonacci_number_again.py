# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    pisano = [0, 1]
    period = 0
    for i in range(2, 7 * m):
        pisano.append((pisano[i - 2] + pisano[i - 1]) % m)
        if pisano[i - 1] == 0 and pisano[i] == 1:
            period = len(pisano) - 2
            break


    fib = n % period
    res = [0, 1]
    for i in range(2, fib + 1):
        res.append(res[i - 2] + res[i - 1])
    return res[fib] % m






if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
