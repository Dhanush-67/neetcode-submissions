class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        res.append(intervals[0])

        for interval in intervals[1:]:
            prev = res[-1]

            if prev[1] >= interval[0]:
                res[-1][1] = max(prev[1], interval[1])
            else:
                res.append(interval)

        return res

        