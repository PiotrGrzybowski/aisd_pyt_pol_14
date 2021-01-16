from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        index = 0
        biggest_space = 0

        while index < len(seats):
            if seats[index] == 0:
                candidate = index
                while candidate < len(seats) and seats[candidate] == 0:
                    candidate += 1

                if index == 0 or candidate == len(seats):
                    space = candidate - index
                else:
                    space = (candidate - index + 1) // 2

                if space > biggest_space:
                    biggest_space = space

                index = candidate
            else:
                index += 1

        return biggest_space
