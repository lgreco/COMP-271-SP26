from __future__ import annotations
from enhanced_linked_list import EnhancedLinkedList
from node import Node


class Queue(EnhancedLinkedList):

    def __init__(self):
        super().__init__()

    def enqueue(self, Node) -> None:
        self.add(Node)

    def dequeue(self) -> Node | None:
        # Grab whatever is in front of the queue. If could be just
        # a plain None. That's fine to return too, indicating that
        # the queue is empty.
        node_at_the_front = self._head
        # We may have some work to do if the item in the front of 
        # the queue is an actual node.
        if node_at_the_front is not None:
            # Move the head pointer to the next object -- even if
            # it's a None.
            self._head = self._head.get_next()
            # Adjust size down
            self._size -= 1
            # If we just emptied the queue, remember to 
            # move the tail pointer to None as well.
            if self._size == 0:
                self._tail = None
        # Return the removed object
        return node_at_the_front
        


# Brutally naive testing
if __name__ == "__main__":
    test = Queue()
    test.enqueue(Node("LEO"))
    print(test.dequeue())
    print(test.dequeue())