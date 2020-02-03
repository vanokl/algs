# python3

def fibonacci_number(n):
    assert 0 <= n <= 45


    res = [0, 1]
    if n < 2:
        return res[n]
    for i in range(2, n + 1):
        res.append(res[i - 1] + res[i - 2])
    return res[n]

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
