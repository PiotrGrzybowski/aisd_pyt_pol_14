from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Optional

from structures.own_types import T


class List(ABC, Generic[T]):
    @abstractmethod
    def length(self) -> int:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    def __len__(self):
        return self.length()


class LinkedList(List[T]):
    @dataclass
    class Node(Generic[T]):
        value: T
        next: Optional[LinkedList.Node] = None

    def __init__(self) -> None:
        self.head = None

    def length(self) -> int:
        result = 0
        pointer = self.head

        while pointer is not None:
            result += 1
            pointer = pointer.next

        return result

    def __str__(self) -> str:
        result = ''
        pointer = self.head

        while pointer is not None:
            result += str(pointer.value)
            pointer = pointer.next

            if pointer is not None:
                result += ', '
        return f'[{result}]'
