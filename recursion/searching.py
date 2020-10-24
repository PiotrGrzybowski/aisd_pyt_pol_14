from typing import List


def search(values: List[int], target: int) -> int:
    index = 0
    while index < len(values) and values[index] != target:
        index += 1

    return index if index < len(values) else -1


# def binary_search(values: List[int], target: int) -> int:
def binary_search(values: List[int], target: int, left: int, right: int):
    if right >= left:
        middle = (left + right) // 2

        if values[middle] == target:
            return middle
        elif values[middle] > target:
            return binary_search(values, target, left, middle - 1)
        else:
            return binary_search(values, target, middle + 1, right)
    else:
        return -1


if __name__ == '__main__':
    numbers = [5, 7, 9, 10, 14, 33]

    length = 100000000
    values = list(range(1, length + 1))
    print(search(values, length))

    # print(binary_search(values, target=length, left=0, right=len(values) - 1))
