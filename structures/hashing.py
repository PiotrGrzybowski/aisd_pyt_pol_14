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
        self.hashes = {
            str: self.hash_string
        }

    def hash(self, value: Any) -> int:
        return self.hashes[type(value)](value)

    def hash_string(self, value: str) -> int:
        result = 7
        prime = 31

        for sign in value:
            result = result * prime + ord(sign)

        return result
