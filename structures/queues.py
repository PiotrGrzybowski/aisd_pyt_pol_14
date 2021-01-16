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

    @abstractmethod
    def front(self) -> T:
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


class FifoQueue(AbstractQueue[T]):
    class EmptyQueueError(Exception):
        def __init__(self) -> None:
            super().__init__('You can not pop from empty Queue.')

    @dataclass
    class Node(Generic[T]):
        value: T
        next: Optional[FifoQueue.Node[T]] = None

    def __init__(self):
        self.head = None
        self.end = None

    def push(self, element: T) -> None:
        node = FifoQueue.Node[T](element)

        if self.head is None:
            self.head = node
            self.end = node
        else:
            self.end.next = node
            self.end = self.end.next

    def pop(self) -> T:
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value
        else:
            raise FifoQueue.EmptyQueueError()

    def front(self) -> T:
        if self.head:
            return self.head.value
        else:
            raise FifoQueue.EmptyQueueError()


if __name__ == '__main__':
    q = FifoQueue[int]()
    q.push('ala')

