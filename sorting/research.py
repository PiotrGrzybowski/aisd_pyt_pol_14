import json

from abc import ABC, abstractmethod

from sorting.algorithms import generate_ordered_list, generate_reversed_list, generate_random_list

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

    for length in range(1, max_length + 1):
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
    algorithm = BubbleSort()
    simulate(algorithm, 100)




    # length = 1000
    # ordered_list = generate_ordered_list(length)
    # reversed_list = generate_reversed_list(length)
    # random_list = generate_random_list(length, 0, 10)
    #
    # experiment_list = random_list
    # algorithm = BubbleSort()
    # algorithm.sort(experiment_list)
    # print(algorithm.comparisons)
    # print(algorithm.__class__.__name__)
