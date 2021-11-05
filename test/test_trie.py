import unittest

from syllabicator.trie import *

class TestNode(unittest.TestCase):
    def test_insert(self):
        n = Node("a")
        n.insert("xy", 1)
        self.assertEqual(repr(n),
                         "'a': (None, {'x': (None, {'y': (1, set())})})",
                         "Wrong Trie structure after insert")

    def test_longestMatch(self):
        n = Node("a")
        n.insert("xy")
        self.assertEqual(n.longestMatch("xyz"), "axy", "match not found or incorrect")
        self.assertEqual(n.longestMatch("qwe"), "", "match found where there is none")

    def test_get(self):
        n = Node("a")
        n.insert("xyz", 5)
        self.assertEqual(n.get("xyz"), 5, "item not found")
        self.assertEqual(n.get("qwe"), None, "nonexistent item found")

    def test_delete(self):
        n = Node("a")
        n.insert("xy", 1)
        n.insert("x")
        n.delete("x")
        self.assertEqual(repr(n),
                         "'a': (None, {'x': (None, {'y': (1, set())})})",
                         "Wrong Trie structure after delete")
        self.assertRaises(KeyError,
                          lambda x: n.delete(x), "qwe")


if __name__ == "__main__":
    unittest.main()
