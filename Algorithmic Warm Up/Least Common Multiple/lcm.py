# python3


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple

def gcd(a, b):
    if b == 0:
        return a
    if a > b:
        return gcd(b, a % b)
    else:
        return gcd(a, b % a)

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    gcd1 = gcd(a, b)
    return a * b // gcd1



if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
