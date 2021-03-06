# python3
import math
from itertools import permutations





def largest_number(numbers):
    salary = []
    while len(numbers) != 0:
        max_number = -math.inf
        ind = 0
        for i in range(len(numbers)):
            if numbers[i] > max_number:
                max_number = numbers[i]
                max_ind = i
        salary.append(max_number)
        numbers.pop(max_ind)
    res = ''
    for i in salary:
        res += str(i)

    return int(res)

if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
