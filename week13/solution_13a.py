from __future__ import annotations

from week09.node import Node


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

    def remove(self, value: str) -> bool:
        """Removes the first node with the given value from the linked list."""
        # We need to keep track of the previous node in order to update the
        # next reference when we remove a node. We also need to keep track of
        # whether we have removed a node or not, so that we can stop the loop
        # once we have removed a node.
        previous = None
        # We also need to keep track of the current node as we traverse 
        # the list.
        current = self._head
        # We also need to keep track of whether we have removed a node 
        # or not, so that we can stop the loop once we have removed a node.
        removed = False
        # We will loop through the list until we find the node with the 
        # given value or we reach the end of the list.
        while current != None and not removed:
            # If the current node has the value we are looking for, 
            # we need to remove it from the list.
            if current.get_value() == value:
                if previous == None:
                    # If the previous node is None, it means we are removing 
                    # the head of the list.
                    self._head = current.get_next()
                else:
                    # If the previous node is not None, it means we are 
                    # removing a node that is not the head of the list.
                    # In this case, we need to update the next reference 
                    # of the previous node to skip the current node.
                    previous.set_next(current.get_next())
                # If the current node is the tail of the list, we 
                # need to update the tail reference.
                if current == self._tail:
                    self._tail = previous
                # Update the size of the object
                self._size -= 1
                # Set the removed flag to True to indicate that we 
                # have removed a node. This will end the loop.
                removed = True
            else:
                # If the current node does not have the value we are 
                # looking for, we need to move to the next node. 
                # In this case, we need to update the previous reference 
                # to the current node before we move to the next node.
                previous = current
                current = current.get_next()
        # Done
        return removed
    
    def remove_all(self, value: str) -> int:
        """Removes all nodes with the given value from the linked list."""
        # We can simply call the remove method repeatedly until it 
        # returns False, which means there are no more nodes with the given 
        # value to remove. We also need to keep track of how many nodes we 
        # have removed, so that we can return that number at the end.
        nodes_removed:int = 0
        while self.remove(value):
            nodes_removed += 1
        return nodes_removed