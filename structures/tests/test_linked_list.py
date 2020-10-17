from unittest import TestCase, main

from structures.lists import LinkedList


class TestLinkedList(TestCase):
    def test_init_without_elements(self):
        values = LinkedList[int]()

        self.assertIsNone(values.head)


if __name__ == '__main__':
    main()
