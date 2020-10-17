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

    def test_append_to_empty_list(self):
        values = LinkedList[int]()
        values.append(9)

        self.assertEqual(1, len(values))
        self.assertEqual('[9]', str(values))

    def test_append_to_many_elements_list(self):
        values = LinkedList[int]()
        values.head = LinkedList.Node[int](9, LinkedList.Node[int](5, LinkedList.Node[int](1)))
        values.append(0)

        self.assertEqual('[9, 5, 1, 0]', str(values))
        self.assertEqual(4, len(values))

    def test_init_with_elements(self):
        values = LinkedList[int](9, 5, 1)

        self.assertEqual('[9, 5, 1]', str(values))

    def test_get_item_first_element(self):
        values = LinkedList[int](9, 5, 1)

        self.assertEqual(9, values[0])

    def test_get_item_last_element(self):
        values = LinkedList[int](9, 5, 1)

        self.assertEqual(1, values[2])

    def test_get_item_out_of_range(self):
        values = LinkedList[int](9, 5, 1)

        with self.assertRaises(IndexError):
            value = values[200]


if __name__ == '__main__':
    main()
