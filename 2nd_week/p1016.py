import math


def solve():
    minimum, maximum = map(int, input().split())
    numbers = [1 for _ in range(minimum, maximum + 1)]
    min_sq = int(math.sqrt(maximum))
    min_list = [v ** 2 for v in range(2, min_sq + 1)]

    max_index = len(numbers)
    for mini in min_list:
        cur_index = math.ceil(minimum / mini) * mini - minimum
        while cur_index < max_index:
            numbers[cur_index] = 0
            cur_index += mini

    print(sum(numbers))


solve()
