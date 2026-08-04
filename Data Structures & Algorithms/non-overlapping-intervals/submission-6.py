class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = [intervals[0]]
        count = 0

        for i in intervals[1:]:
            interval = res[-1]

            if i[0] < interval[1]:
                if i[1] <= interval[1]:
                    res[-1][1] = i[1]
                count += 1
                
            else:
                res.append(i)

        return count
        