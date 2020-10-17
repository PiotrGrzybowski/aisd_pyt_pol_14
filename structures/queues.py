from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Optional

from structures.own_types import T


class AbstractQueue(ABC, Generic[T]):
    @abstractmethod
    def push(self, element: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T:
        pass


class Stack(AbstractQueue[T]):
    class EmptyStackError(Exception):
        def __init__(self) -> None:
            super().__init__('You can not pop from empty Stack.')

    @dataclass
    class Node(Generic[T]):
        value: T
        next: Optional[Stack.Node[T]] = None

    def __init__(self):
        self.top = None

    def push(self, element: T) -> None:
        node = Stack.Node[T](element)

        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self) -> T:
        if self.top is not None:
            value = self.top.value
            self.top = self.top.next
            return value
        else:
            raise Stack.EmptyStackError()

    def front(self) -> T:
        if self.top:
            return self.top.value
        else:
            raise Stack.EmptyStackError()

    def __bool__(self):
        return self.top is not None
