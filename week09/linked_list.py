from node import Node


class LinkedList:
    """A simple linked list data structure."""

    def __init__(self):
        # Fields below are designated as protected (single
        # unferscore) instead of private (double underscore).
        # The objective is still to show other users that 
        # the fields are for internal-use only. And at the 
        # same time to avoid the complications from double
        # underscore name mangling.
        self._head = None
        self._tail = None
        self._size = 0

    def __str__(self):
        """Tragically simple string rendering"""
        result = ""
        current = self._head
        while current != None:
            result += str(current) + " "
            current = current.get_next()
        return result

    def add(self, new_node: Node) -> None:
        """Adds a new node to the linked list."""
        if new_node is not None:
            # Operate only if there is something given to
            # us to add.
            if self._head == None:
                self._head = new_node
            else:
                self._tail.set_next(new_node)
            # In either case, update the tail
            self._tail = new_node
            # Update the size of the object
            self._size += 1
    
    def add_with_string(self, value:str) -> None:
        if value is not None:
            self.add(Node(value))


# -------------------------
# Brutally naive testing
# -------------------------
if __name__ == "__main__":
    test = LinkedList()
    test.add(Node(1))
    test.add(Node(2))
    print(test)
