# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    if len(segments) == 0:
        return 0

    segments.sort(key=lambda x: x[1])

    current_dot = 0
    n = len(segments) - 1
    dots_list = [segments[current_dot][1]]
    while current_dot < n:
        last_dot = current_dot
        current_dot += 1
        while (segments[current_dot][0] <= segments[last_dot][1]) and (current_dot < n):
            current_dot += 1
        if segments[current_dot][0] > segments[last_dot][1]:
            dots_list.append(segments[current_dot][1])

    return dots_list


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
