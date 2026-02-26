########################################################################
#                                       #                              #
# TESTING CODE FOR WEEK 06 ASSIGNMENT.  #  Testing code requires class #
# ADD THIS CODE AFTER YOUR WEEKO6 CODE. #  LinkedList to be present.   #
# DO NOT MODIFY THE TESTING CODE.       #                              #
#                                       #                              #
########################################################################

import unittest  # Authorized import for unit testing
from time import time_ns  # Authorized import for timing


################################################################################
# MOVE THE FOLLOWING IMPORT FROM __FUTURE TO THE TOP OF YOUR                   #
################################################################################
from __future__ import annotations  # Authorized import for type hints

from week06 import Node, LinkedList  # Authorized import for testing


class Node:

    def __init__(self, value: str) -> None:
        self.__value: str = value
        self.__next: Node | None = None

    def __str__(self) -> str:
        return f"{self.__value}"

    def has_next(self) -> bool:
        return self.__next is not None

    def get_next(self) -> Node | None:
        return self.__next

    def set_next(self, next: Node) -> None:
        self.__next = next

    def get_value(self) -> str:
        return self.__value


class TsilDeknil:
    """Old Linked List class, for testing purposes only."""

    def __init__(self) -> None:
        self.__head: Node | None = None

    def __str__(self) -> str:
        return ""

    def add(self, value: str) -> None:
        new_node: Node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            current: Node = self.__head
            while current.has_next():
                current = current.get_next()
            current.set_next(new_node)

    def count(self) -> int:
        counter: int = 0
        current: Node = self.__head
        while current is not None:
            counter += 1
            current = current.get_next()
        return counter


class TestLinkedListInsert(unittest.TestCase):
    # --- helpers -------------------------------------------------------------

    def make_list(self, *values: str):
        ll = LinkedList()
        for v in values:
            ll.add(v)
        return ll

    def tsil_ekam(self, *values: str):
        tt = TsilDeknil()
        for v in values:
            tt.add(v)
        return tt

    def populate(self, object, N):
        for i in range(N):
            object.add(f"Node{i}")

    def time_add(self, object, N):
        start_time = time_ns()
        self.populate(object, N)
        elapsed_time = time_ns() - start_time
        return elapsed_time / N

    def time_count(self, object, N):
        self.populate(object, N)
        start_time = time_ns()
        c = object.count()
        elapsed_time = time_ns() - start_time
        return elapsed_time / N

    # --- tests ---------------------------------------------------------------

    def test_insert_into_empty_list_returns_false_and_no_change(self):
        ll = LinkedList()
        self.assertEqual("Empty List", str(ll))
        self.assertEqual(0, ll.count())

        result = ll.insert("X", "A")
        self.assertFalse(result)
        self.assertEqual("Empty List", str(ll))
        self.assertEqual(0, ll.count())

    def test_insert_missing_after_value_returns_false_and_no_change(self):
        ll = self.make_list("A", "B", "C")
        before_str = str(ll)
        before_count = ll.count()

        result = ll.insert("X", "NOPE")
        self.assertFalse(result)
        self.assertEqual(before_str, str(ll))
        self.assertEqual(before_count, ll.count())

    def test_insert_after_head(self):
        ll = self.make_list("A", "B", "C")
        result = ll.insert("A2", "A")

        self.assertTrue(result)
        self.assertEqual("A → A2 → B → C", str(ll))
        self.assertEqual(4, ll.count())

    def test_insert_in_middle(self):
        ll = self.make_list("A", "B", "C")
        result = ll.insert("B2", "B")

        self.assertTrue(result)
        self.assertEqual("A → B → B2 → C", str(ll))
        self.assertEqual(4, ll.count())

    def test_insert_after_tail_updates_end_of_list(self):
        ll = self.make_list("A", "B", "C")
        result = ll.insert("C2", "C")

        self.assertTrue(result)
        self.assertEqual("A → B → C → C2", str(ll))
        self.assertEqual(4, ll.count())

        # A follow-up insert-after-tail should now treat C2 as the tail
        result2 = ll.insert("C3", "C2")
        self.assertTrue(result2)
        self.assertEqual("A → B → C → C2 → C3", str(ll))
        self.assertEqual(5, ll.count())

    def test_insert_after_first_match_only_when_duplicates_exist(self):
        ll = self.make_list("A", "B", "C", "B")  # duplicate B at the end
        result = ll.insert("X", "B")

        self.assertTrue(result)
        # Must insert after the FIRST "B", not the last one
        self.assertEqual("A → B → X → C → B", str(ll))
        self.assertEqual(5, ll.count())

    def test_failed_insert_does_not_mutate_list(self):
        ll = self.make_list("A", "B", "C")
        snapshot_str = str(ll)
        snapshot_count = ll.count()

        self.assertFalse(ll.insert("Y", "ZZZ"))
        self.assertEqual(snapshot_str, str(ll))
        self.assertEqual(snapshot_count, ll.count())

    def test_o1_ops_with_dict(self):
        ll = self.make_list("A", "B", "C")
        self.assertTrue(len(ll.__dict__) > 1, "Problem 1 or 2 probably incomplete")

    _N = 1024

    def test_o1_ops_for_add(self):
        ll = self.make_list("A")
        tt = self.tsil_ekam("A")
        o1_avg = self.time_add(ll, self._N)
        on_avg = self.time_add(tt, self._N)
        expect = o1_avg < (on_avg / 10)
        self.assertTrue(expect, "Problem 1 probably incomplete")

    def test_o1_ops_for_count(self):
        ll = self.make_list("A")
        tt = self.tsil_ekam("A")
        o1_avg = self.time_count(ll, self._N)
        on_avg = self.time_count(tt, self._N)
        expect = o1_avg < (on_avg / 10)
        self.assertTrue(expect, "Problem 2 probably incomplete")


################################################################################
# fmt: off
#
# If you test in a .PY file, uncomment TEST-LINE-1 and TEST-LINE-2 and
# comment out TEST-LINE-3 to run the tests.

# if __name__ == "__main__":              #   TEST-LINE-1
#    unittest.main()                     #   TEST-LINE-2

# If you test in a Jupyter notebook, comment out TEST-LINE-1 and TEST-LINE-2
# and uncomment TEST-LINE-C to run the tests in the notebook.

# unittest.main(argv=[''], exit=False)    #   TEST-LINE-3

################################################################################
