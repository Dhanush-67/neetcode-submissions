class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        intervals.sort(key=lambda x: x.start)

        for i in range(1, n):
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True