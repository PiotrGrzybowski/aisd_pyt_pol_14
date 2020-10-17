from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Optional

from structures.own_types import T


class List(ABC, Generic[T]):
    @abstractmethod
    def __str__(self) -> str:
        pass


class LinkedList(List[T]):
    @dataclass
    class Node(Generic[T]):
        value: T
        next: Optional[LinkedList.Node] = None

    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        pass
