from abc import ABC, abstractmethod
from typing import Optional


class Node(ABC):
    def __init__(self, left: Optional['Node'], right: Optional['Node']):
        self.left: Optional['Node'] = left
        self.right: Optional['Node'] = right

    @abstractmethod
    def leftmost(self) -> 'Node':
        pass

    @abstractmethod
    def rightmost(self) -> 'Node':
        pass

    @abstractmethod
    def chain(self):
        pass

    @abstractmethod
    def magnitude(self) -> int:
        pass

    @abstractmethod
    def can_explode(self, depth: int) -> bool:
        pass

    @abstractmethod
    def explode(self, depth: int) -> bool:
        pass

    @abstractmethod
    def can_split(self) -> bool:
        pass

    @abstractmethod
    def split(self) -> bool:
        pass

    @abstractmethod
    def reduce(self):
        pass
