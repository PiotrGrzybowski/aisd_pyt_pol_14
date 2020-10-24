from typing import List


def factorial(n: int):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_iterative(n: int):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def sum_list_recursively(values: List[int]):
    if not values:
        return 0
    else:
        return values[0] + sum_list_recursively(values[1:])


if __name__ == '__main__':
    print(sum_list_recursively([1, 10, 19]))
