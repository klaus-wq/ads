from linked_list import *
import unittest

class TestLinkedList(unittest.TestCase):

    def test_delete(self):
        s_list = LinkedList()
        s_list.delete(12)
        self.assertEqual(s_list.len(), 0)
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(12))
        s_list.delete(12, True)
        self.assertEqual(s_list.len(), 0)
        s_list.delete(12)
        self.assertEqual(s_list.len(), 0)
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(56))
        s_list.add_in_tail(Node(78))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(78))
        s_list.add_in_tail(Node(12))
        s_list.delete(12)
        self.assertEqual(s_list.head.value,56)
        self.assertEqual(s_list.tail.value,12)

    def test_find_all(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(56))
        s_list.add_in_tail(Node(78))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(78))
        s_list.add_in_tail(Node(12))
        self.assertEqual(len(s_list.find_all(78)),2)
        self.assertEqual(len(s_list.find_all(56)),1)
        self.assertEqual(len(s_list.find_all(100)),0)

    def test_len(self):
        s_list = LinkedList()
        self.assertEqual(s_list.len(), 0)
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(56))
        s_list.add_in_tail(Node(78))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(78))
        s_list.add_in_tail(Node(12))
        self.assertEqual(s_list.len(), 6)

    def test_clean(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(56))
        s_list.add_in_tail(Node(78))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(78))
        s_list.add_in_tail(Node(12))
        s_list.clean()
        self.assertEqual(s_list.len(), 0)

    def test_insert(self):
        s_list = LinkedList()
        s_list.insert(None, Node(12))
        self.assertEqual(s_list.head.value, 12)
        s_list = LinkedList()
        s_list.add_in_tail(Node(55))
        s_list.insert(Node(55), Node(15))
        self.assertEqual(s_list.head.value, 55)
        self.assertEqual(s_list.tail.value, 15)
        s_list = LinkedList()
        s_list.add_in_tail(Node(55))
        s_list.add_in_tail(Node(75))
        s_list.add_in_tail(Node(55))
        s_list.insert(None, Node(15))
        self.assertEqual(s_list.head.value, 15)

if __name__ == "__main__":
  unittest.main()
