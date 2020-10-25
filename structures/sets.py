from abc import ABC, abstractmethod
from typing import Any, List

from structures.hashing import HashFunction, NaiveHashFunction
from structures.lists import LinkedList


class Set(ABC):
    @abstractmethod
    def add(self, value: Any) -> None:
        pass

    @abstractmethod
    def remove(self, value: Any) -> None:
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def __contains__(self, item: Any):
        pass


class HashSet(Set):
    def __init__(self, hash_function: HashFunction, initial_buckets_size: int = 4, payload_factor: float = 0.75, increase_factor: int = 2):
        self.hash_function = hash_function
        self.initial_buckets_size = initial_buckets_size
        self.payload_factor = payload_factor
        self.increase_factor = increase_factor
        self.buckets = self._create_empty_buckets(self.initial_buckets_size)

    def add(self, value: Any) -> None:
        hash_value = self.hash_function.hash(value)
        bucket_index = hash_value % len(self.buckets)
        self.buckets[bucket_index].append(value)

    def remove(self, value: Any) -> None:
        pass

    def clear(self):
        self.buckets = self._create_empty_buckets(self.initial_buckets_size)

    def __contains__(self, item: Any):
        pass

    def _create_empty_buckets(self, buckets_count: int) -> List[LinkedList]:
        return [LinkedList() for _ in range(buckets_count)]

    def buckets_str(self) -> str:
        return '\n'.join([f"{i:3} -> {str(bucket)}" for i, bucket in enumerate(self.buckets)])


if __name__ == '__main__':
    naive_hash_function = NaiveHashFunction()
    values = HashSet(naive_hash_function)

    values.add("Piotr")
    values.add("Ola")
    values.add("Mark")
    print(values.buckets_str())
