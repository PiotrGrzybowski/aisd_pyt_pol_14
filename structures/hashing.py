from abc import ABC, abstractmethod
from typing import Any


class HashFunction(ABC):
    @abstractmethod
    def hash(self, value: Any) -> int:
        pass


class NaiveHashFunction(HashFunction):
    def hash(self, value: Any) -> int:
        return 2

    def hash_string(self, value: str) -> int:
        pass


class PrimeHashFunction(HashFunction):
    def __init__(self):
        self.hashes = {}
    def hash(self, value: Any) -> int:
        pass

    def hash_string(self, value: str) -> int:
        pass
