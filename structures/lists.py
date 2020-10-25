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
    def append(self, element: T) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        pass

    @abstractmethod
    def __setitem__(self, index: int, element: T) -> None:
        pass

    def __len__(self):
        return self.length()


class LinkedList(List[T]):
    @dataclass
    class Node(Generic[T]):
        value: T
        next: Optional[LinkedList.Node] = None

    def __init__(self, *args: T) -> None:
        self.head = None
        self._append_init_elements(args)

    def _append_init_elements(self, args):
        if args:
            for element in args:
                self.append(element)

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

    def append(self, element: T) -> None:
        node = LinkedList.Node[int](element)

        if self.head is None:
            self.head = node
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next

            pointer.next = node

    def __getitem__(self, index: int) -> T:
        pointer = self.head
        pointer_index = 0

        while pointer is not None and pointer_index < index:
            pointer = pointer.next
            pointer_index += 1

        if pointer is not None:
            return pointer.value
        else:
            raise IndexError("list index out of range")

    def __setitem__(self, index: int, value: T) -> None:
        i = 0
        pointer = self.head

        while pointer is not None and i < index:
            pointer = pointer.next
            i += 1

        if pointer is not None and i == index:
            pointer.value = value
        else:
            raise IndexError(f'pop index out of range')

    def index(self, element: T) -> int:
        result = -1
        pointer = self.head
        index = 0
        while pointer and result == -1:
            if pointer.value == element:
                result = index
            pointer = pointer.next
            index += 1

        if result == -1:
            raise ValueError(f'{str(element)} is not in list')
        else:
            return result

    def contains(self, element: T) -> bool:
        try:
            return self.index(element) > -1
        except ValueError:
            return False

    def __contains__(self, element: T) -> bool:
        return self.contains(element)