from typing import List


def delivery_presents_iteratively(houses: List[str]) -> None:
    for house in houses:
        print(f'Delivering presents to {house}')


def delivery_presents_recursively(houses: List[str]) -> None:
    if len(houses) == 1:
        house = houses[0]
        print(f'Delivering presents to {house}')
    else:
        middle = len(houses) // 2
        first_half = houses[:middle]
        second_half = houses[middle:]

        delivery_presents_recursively(first_half)
        delivery_presents_recursively(second_half)


if __name__ == '__main__':
    houses = ["Piotr's House", "Ola's House", "John's House", "Ada's House"]
    houses = []
    delivery_presents_recursively(houses)
