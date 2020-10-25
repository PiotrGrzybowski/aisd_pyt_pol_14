from abc import ABC, abstractmethod
from typing import Any, List

from structures.hashing import HashFunction, NaiveHashFunction, PrimeHashFunction
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
    def __init__(self, hash_function: HashFunction, initial_buckets_size: int = 4, payload_factor: float = 0.75,
                 increase_factor: int = 2):
        self.hash_function = hash_function
        self.initial_buckets_size = initial_buckets_size
        self.payload_factor = payload_factor
        self.increase_factor = increase_factor
        self.buckets = self._create_empty_buckets(self.initial_buckets_size)

        self.size = 0

    def add(self, value: Any) -> None:
        if self.size / len(self.buckets) >= self.payload_factor:
            self._increase_bucket_count(self.increase_factor * len(self.buckets))
        hash_value = self.hash_function.hash(value)
        bucket_index = hash_value % len(self.buckets)
        self.buckets[bucket_index].append(value)
        self.size += 1

    def _increase_bucket_count(self, target_bucket_count) -> None:
        new_buckets = self._create_empty_buckets(target_bucket_count)

        for bucket in self.buckets:
            for value in bucket:
                hash_value = self.hash_function.hash(value)
                bucket_index = hash_value % len(new_buckets)
                new_buckets[bucket_index].append(value)

        self.buckets = new_buckets

    def remove(self, value: Any) -> None:
        pass

    def clear(self):
        self.size = 0
        self.buckets = self._create_empty_buckets(self.initial_buckets_size)

    def __contains__(self, value: Any):
        hash_value = self.hash_function.hash(value)
        bucket_index = hash_value % len(self.buckets)
        return value in self.buckets[bucket_index]

    def _create_empty_buckets(self, buckets_count: int) -> List[LinkedList]:
        return [LinkedList() for _ in range(buckets_count)]

    def buckets_str(self) -> str:
        return '\n'.join([f"{i:3} -> {str(bucket)}" for i, bucket in enumerate(self.buckets)])


import string
import random


def generate_random_str(length: int):
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=length))


if __name__ == '__main__':
    naive_hash_function = PrimeHashFunction()
    values = HashSet(naive_hash_function)

    values.add("Piotr")
    values.add("Piotr")
    values.add("Piotr")
    values.add("Aleksandra")
    values.add("Ola")
    values.add("Majestic")
    values.add("Majestic454gx2")
    values.add("a")
    values.add("basd")
    values.add("cdsdgs")

    for i in range(10000):
        values.add(generate_random_str(30))

    print(values.buckets_str())
    print("Adam" in values)
