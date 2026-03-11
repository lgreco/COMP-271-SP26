from __future__ import annotations
from linked_list import LinkedList
from node import Node


class EnhancedLinkedList(LinkedList):

    def __init__(self):
        super().__init__()

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size
    
    def peek(self) -> Node | None:
        return None if self.is_empty() else self._head
    