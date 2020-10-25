from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) < 2:
        return intervals
    else:
        intervals.sort(key=lambda interval: interval[0])
        result = []
        current_interval = intervals[0]
        result.append(current_interval)

        for interval in intervals[1:]:
            current_interval_end = current_interval[1]
            next_interval_begin = interval[0]
            next_interval_end = interval[1]

            if next_interval_begin <= current_interval_end:
                current_interval[1] = max(current_interval_end, next_interval_end)
            else:
                result.append(interval)
                current_interval = interval

        return result


if __name__ == '__main__':
    case = [[13, 15], [2, 3], [8, 10], [2, 4], [8, 11], [3, 6]]
    result = merge_intervals(case)
    print(result)
