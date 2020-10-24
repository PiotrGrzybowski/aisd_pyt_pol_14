import json
import sys
from abc import ABC, abstractmethod
from typing import Any, List
import random

from tqdm import tqdm

from sorting.algorithms import generate_ordered_list, generate_reversed_list, generate_random_list

sys.setrecursionlimit(1500)
REVERSED = 'reversed'
ORDERED = 'ordered'
RANDOM = 'random'


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
    def sort(self, values: List[Any]) -> None:
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


class QuickSort(SortingAlgorithm):
    def partition(self, values: List[Any], left: int, right: int) -> int:
        pivot_index = random.randint(left, right)
        values[right], values[pivot_index] = values[pivot_index], values[right]
        pivot = values[right]
        j = left - 1

        for i in range(left, right):
            if self.lt(values[i], pivot):
                j += 1
                values[i], values[j] = values[j], values[i]
        j += 1
        values[j], values[right] = values[right], values[j]
        return j

    def sort(self, values: List[Any]) -> None:
        self.comparisons = 0

        def sort_help(left: int, right: int) -> None:
            if self.lt(left, right):
                index = self.partition(values, left, right)
                sort_help(left, index - 1)
                sort_help(index + 1, right)

        sort_help(0, len(values) - 1)


def simulate(algorithm: SortingAlgorithm, max_length):
    """
    Przyjmuje algorytm, za pomocą którego zostanie wykonane sortowanie
    list: uporządkowanej, odwrotnie uporządkowanej i losowo uporządkowanej o długościach
    od 1 do max_lenght.

    {'ordered': {1: y, 2: x, ..., 1000: z}
     'reversed': {1: y, 2: x, ..., 1000: z}
     'random': {1: y, 2: x, ..., 1000: z}
    }

    Kroki do wykonania:
    - utwórz słownik wynikowy o formacie:
      {'ordered': {}
      'reversed': {}
      'random': {}}
    - Pętla for length in range(1, max_length)
      - wygeneruj trzy listy wykorzystując wcześniej zdefiniowane funkcje dla aktualnej wartości length:
        * ordered_list
        * reversed_list
        * random_list
      - dla każde z nich wykonaj sortowanie algorytmem przekazanym jako argument: algorithm
      - do słownika wynikowego pod odpowiedni klucz (losowa, uporządkowane, odwrotnie uporządkowana)
        dodaj nowy wynik gdzie klucz będzie długością aktualnie sortowanej listy a wartością liczba wykonanych porównań w czasie sortowania.

    Zapisz słownik do obiektu pickle o nazwie: f'{algorithm.__class__.__name__}_{max_length}.json'
    Przykładowa zapisana nazwa pliku to: BubbleSort_1000.json
    """

    result = {
        ORDERED: {},
        RANDOM: {},
        REVERSED: {}
    }

    for length in tqdm(range(1, max_length + 1)):
        ordered_list = generate_ordered_list(length)
        algorithm.sort(ordered_list)
        result[ORDERED][length] = algorithm.comparisons

        reversed_list = generate_reversed_list(length)
        algorithm.sort(reversed_list)
        result[REVERSED][length] = algorithm.comparisons

        random_list = generate_random_list(length, 0, 10)
        algorithm.sort(random_list)
        result[RANDOM][length] = algorithm.comparisons

    filename = f'{algorithm.__class__.__name__}_{max_length}.json'
    with open(filename, 'w') as f:
        json.dump(result, f, indent=4, sort_keys=True)


if __name__ == '__main__':
    algorithm = QuickSort()
    simulate(algorithm, 2000)

    # length = 1000
    # ordered_list = generate_ordered_list(length)
    # reversed_list = generate_reversed_list(length)
    # random_list = generate_random_list(length, 0, 10000)
    #
    # experiment_list = random_list
    # print(ordered_list)
    # algorithm = QuickSort()
    # algorithm.sort(experiment_list)
    # print(experiment_list)

