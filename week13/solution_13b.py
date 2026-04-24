from __future__ import annotations


class WeirdoBST:
    """Store string values in a BST, where the tree is represented internally
    as a Python list using the heap-style index arithmetic. The API is:

    `insert(self, value: str) -> None` — insert a string, preserving the BST
    ordering (left subtree < node < right subtree). Assume no duplicates for
    simplicity, or decide on a sensible policy and document it.

    `search(self, value: str) -> bool` — return whether the string is present.

    `__len__(self)` — return $n$, the number of actual strings stored (not the
    length of the underlying array).

    `__str__(self)` — something useful for printing.

    Implementation Details:

    In `__init__`, make `self._underlying: list[str | None] = []`.
    Don't pre-allocate a size — grow on demand.

    When we need to write at index `i` and `i >= len(self._underlying)`,
    extend the list with `None` values until it's long enough. No need
    to do any elaborate math like exponentiation of logarithms here.

    Insertion is a walk, not a recursion on objects. Start at index `i = 0`.
    If `self._underlying[i]` is `None`, you've found the spot — write the
    value there (growing first if needed). Otherwise compare the incoming
    value to `self._underlying[i]` and step to `2*i + 1` or `2*i + 2`.
    Repeat. The loop terminates when you write into a `None` slot.

    Search is the same walk, minus the writing. Walk from index 0, comparing
    and branching left or right, until you either find the value or step
    off the end of the array (or land on a `None`, which also means
    "not here").

    __len__` is not `len(self._underlying)`. It's the count of non-`None`
    entries. You can compute it on demand with a helper function, or maintain
    a running count in an attribute. Either is fine; the running count is
    faster but easier to get wrong.
    """

    def __init__(self):
        """Initialize an empty BST."""
        # The underlying list will store the tree nodes. Each node is either
        # a string or None (indicating an empty slot). We start with an empty
        # list and grow it as needed when inserting values.
        self._underlying: list[str | None] = []
        # A count of the number of actual strings stored in the BST.
        self._count: int = 0

    def insert(self, value: str) -> None:
        """Insert a string into the BST, preserving the BST ordering."""
        # If the underlying list is empty, we need to add a None to allow
        # for the first insertion at index 0.
        if not self._underlying:
            self._underlying.append(None)
        # Start at the root index.
        i = 0
        # Walk down the tree until we find a None slot to insert the value.
        while i < len(self._underlying) and self._underlying[i] is not None:
            # If the value is less than the current node, go left;
            # otherwise, go right.
            if value < self._underlying[i]:
                i = 2 * i + 1
            else:
                i = 2 * i + 2
            # If we step beyond the current length of the underlying list,
            # we need to extend it.
            if i >= len(self._underlying):
                self._underlying.extend([None] * (i + 1 - len(self._underlying)))
        # Now i is the index of a None slot where we can insert the value.
        self._underlying[i] = value
        # Increment the count of actual strings stored in the BST.
        self._count += 1

    def search(self, value: str) -> bool:
        """Return whether the string is present in the BST."""
        # Start at the root index and walk down the tree, comparing the value
        # to the current node and branching left or right accordingly.
        found = False
        i = 0
        # The loop continues as long as we haven't found the value, 
        # and we haven't stepped off the end of the array, and we haven't 
        # hit a None slot. If we hit a None slot, it means the value is not 
        # present in the BST.
        while (
            not found
            and i < len(self._underlying)
            and self._underlying[i] is not None
        ):
            if self._underlying[i] == value:
                # We've found the value in the BST.
                found = True
            elif value < self._underlying[i]:
                # Go left and continue the search.
                i = 2 * i + 1
            else:
                # Go right and continue the search.
                i = 2 * i + 2
        return found

    def __len__(self):
        """Return the number of actual strings stored in the BST."""
        return self._count

    def __str__(self):
        """Return a string representation of the BST."""
        return str(self._underlying)


# Example usage:
if __name__ == "__main__":
    bst = WeirdoBST()
    bst.insert("a")
    bst.insert("b")
    bst.insert("c")
    bst.insert("d")
    bst.insert("e")
    bst.insert("f")
    bst.insert("g")
    bst.insert("h")
    print(bst)  # Print the underlying list representation of the BST.
    print(len(bst))  # Should print 4, the number of strings stored.
    print(len(bst._underlying))  # The length of the underlying list, which may be larger than 4 due to None slots.