from __future__ import annotations
import unittest
from springbreak import Springbreak

class TestSpringBreak(unittest.TestCase):

    def test_empty_on_init(self):
        test_object = Springbreak()
        self.assertTrue(test_object.count()==0)

    def test_add_items(self):
        test_object = Springbreak()
        test_object.add_item("Chicago")
        self.assertTrue(test_object.count()==1)


# Execute the tests
if __name__=="__main__":
    unittest.main()