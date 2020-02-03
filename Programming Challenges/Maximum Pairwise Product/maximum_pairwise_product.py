# python3

def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    ind1 = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[ind1]:
            ind1 = i
    if ind1 == 0:
        ind2 = 1
    else:
        ind2 = 0
    for j in range(1, len(numbers)):
        if ind1 != j and numbers[j] > numbers[ind2]:
            ind2 = j
    return numbers[ind1] * numbers[ind2]

if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
