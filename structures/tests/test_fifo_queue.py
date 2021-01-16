from unittest import TestCase, main

from structures.new_queues import Queue


class TestLinkedList(TestCase):
    def test_init(self):
        queue = Queue[int]()

        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)
        self.assertEqual(queue.size, 0)

    def test_push(self):
        queue = Queue[int]()
        queue.push(3)

        self.assertEqual(queue.head.value, 3)
        self.assertEqual(queue.tail.value, 3)
        self.assertEqual(queue.size, 1)
        self.assertIsNone(queue.head.next)
        self.assertIsNone(queue.tail.next)


if __name__ == '__main__':
    main()
