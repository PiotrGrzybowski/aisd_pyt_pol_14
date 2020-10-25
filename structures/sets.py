from abc import ABC, abstractmethod
from typing import Any, List

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
    def __init__(self, initial_buckets_size: int = 4, payload_factor: float = 0.75, increase_factor: int = 2):
        self.initial_buckets_size = initial_buckets_size
        self.payload_factor = payload_factor
        self.increase_factor = increase_factor

        self.buckets = self._create_empty_buckets(self.initial_buckets_size)

    def add(self, value: Any) -> None:
        pass

    def remove(self, value: Any) -> None:
        pass

    def clear(self):
        pass

    def __contains__(self, item: Any):
        pass

    def _create_empty_buckets(self, buckets_count: int) -> List[LinkedList]:
        return [LinkedList() for _ in range(buckets_count)]

    def buckets_str(self) -> str:
        return '\n'.join([f"{i:3} -> {str(bucket)}" for i, bucket in enumerate(self.buckets)])


if __name__ == '__main__':
    values = HashSet()
    print(values.buckets_str())
