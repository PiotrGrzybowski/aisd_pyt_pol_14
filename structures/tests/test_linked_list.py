from unittest import TestCase, main

from structures.lists import LinkedList


class TestLinkedList(TestCase):
    def test_init_without_elements(self):
        values = LinkedList[int]()

        self.assertIsNone(values.head)

    def test_length_empty_list(self):
        values = LinkedList[int]()

        self.assertEqual(0, values.length())
        self.assertEqual(0, len(values))

    def test_length_one_element_in_list(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node[int](9)

        self.assertEqual(1, values.length())
        self.assertEqual(1, len(values))

    def test_length_many_elements_in_list(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node[int](9, LinkedList.Node[int](5, LinkedList.Node[int](1)))

        self.assertEqual(3, values.length())
        self.assertEqual(3, len(values))

    def test_str_empty_list(self):
        values = LinkedList[int]()

        self.assertEqual('[]', str(values))

    def test_str_many_elements(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node[int](9, LinkedList.Node[int](5, LinkedList.Node[int](1)))

        self.assertEqual('[9, 5, 1]', str(values))


if __name__ == '__main__':
    main()
