from typing import List


def partition(values: List[int], left: int, right: int) -> int:
    j = left - 1
    pivot = values[j]
    if right > left:
        for i in range(left, right):
            if values[i] <= pivot:
                j += 1
                values[i], values[j] = values[j], values[i]
    else:
        return -1
    return j + 1


def quick_sort(values: List[int], left: int, right: int):
    if right > left:
        index = partition(values, left, right)
        quick_sort(values, left, index - 1)
        quick_sort(values, index + 1, right)


if __name__ == '__main__':
    import random

    values = [7, 6, 5, 4, 3, 2, 1]
    # values = [random.randint(0, 10) for _ in range(100)]
    print(values)
    print(partition(values, 0, len(values) - 1))
    print(values)
