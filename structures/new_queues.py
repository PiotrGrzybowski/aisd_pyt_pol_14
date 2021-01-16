from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Optional

from structures.own_types import T


class EmptyQueueError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


@dataclass
class Node(Generic[T]):
    value: T
    next: Optional[Node[T]] = None


class AbstractQueue(ABC, Generic[T]):
    def __init__(self):
        self.size = 0

    @abstractmethod
    def push(self, element: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T:
        pass

    @abstractmethod
    def front(self) -> T:
        pass

    def __len__(self) -> int:
        return self.size


class Stack(AbstractQueue[T]):
    def __init__(self):
        super().__init__()
        self.head = None

    def push(self, element: T) -> None:
        node = Node[T](element)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self) -> T:
        if self.head is not None:
            value = self.head.value
            self.head = self.head.next
            return value
        else:
            raise EmptyQueueError('Can not pop from empty stack.')

    def front(self) -> T:
        if self.head:
            return self.head.value
        else:
            raise EmptyQueueError('Can not read from empty stack.')

    def __bool__(self):
        return self.head is not None


class Queue(AbstractQueue[T]):
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None

    def push(self, element: T) -> None:
        node = Node[T](element)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

        self.size += 1

    def pop(self) -> T:
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value
        else:
            raise EmptyQueueError('Can not pop from empty queue.')

    def front(self) -> T:
        if self.head:
            return self.head.value
        else:
            raise EmptyQueueError('Can not read from empty queue.')


if __name__ == '__main__':
    a = Queue[int]()
    print(len(a))
    a.push('lul')

