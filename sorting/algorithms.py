from random import randint
from typing import Any, List


def generate_random_list(length, start, end):
    return [randint(start, end) for _ in range(length)]


def generate_ordered_list(length):
    return list(range(length))


def generate_reversed_list(length):
    return list(reversed(range(length)))


def bubble_sort(values: List[Any]) -> None:
    length = len(values)
    for n in range(length):
        for index in range(length - 1):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]


def bubble_sort_2(values: List[Any]) -> None:
    length = len(values)
    n = 0
    swap_occurred = True

    while n < length and swap_occurred:
        swap_occurred = False
        for index in range(length - 1):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
                swap_occurred = True

        n += 1


if __name__ == '__main__':
    length = 100
    ordered_list = generate_ordered_list(length)
    reversed_list = generate_reversed_list(length)
    random_list = generate_random_list(length, 0, 10)

    experiment_list = ordered_list
    bubble_sort_2(experiment_list)
    print(experiment_list)
