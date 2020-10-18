from abc import ABC, abstractmethod

from sorting.algorithms import generate_ordered_list, generate_reversed_list, generate_random_list


class SortingAlgorithm(ABC):
    def __init__(self):
        self.comparisons = 0

    def gt(self, value_1, value_2) -> bool:
        self.comparisons += 1
        return value_1 > value_2

    def gte(self, value_1, value_2) -> bool:
        self.comparisons += 1
        return value_1 >= value_2

    def lt(self, value_1, value_2) -> bool:
        self.comparisons += 1
        return value_1 < value_2

    def lte(self, value_1, value_2) -> bool:
        self.comparisons += 1
        return value_1 <= value_2

    def eq(self, value_1, value_2) -> bool:
        self.comparisons += 1
        return value_1 == value_2

    @abstractmethod
    def sort(self, values):
        pass


class BubbleSort(SortingAlgorithm):
    def sort(self, values):
        self.comparisons = 0
        length = len(values)
        n = 0
        swap_occurred = True

        while n < length and swap_occurred:
            swap_occurred = False
            for index in range(length - 1):
                if self.gt(values[index], values[index + 1]):
                    values[index], values[index + 1] = values[index + 1], values[index]
                    swap_occurred = True

            n += 1


def simulate(algorithm, max_length):
    pass


if __name__ == '__main__':
    length = 1000
    ordered_list = generate_ordered_list(length)
    reversed_list = generate_reversed_list(length)
    random_list = generate_random_list(length, 0, 10)

    experiment_list = random_list
    algorithm = BubbleSort()
    algorithm.sort(experiment_list)
    print(algorithm.comparisons)

