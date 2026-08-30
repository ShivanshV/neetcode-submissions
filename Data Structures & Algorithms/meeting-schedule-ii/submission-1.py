"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x: x.start)
        days = []
        heapq.heappush(days, intervals[0].end)
        for i in range(1, len(intervals)):
            if intervals[i].start >= days[0]:
                heapq.heappop(days)
            heapq.heappush(days,intervals[i].end)
        return len(days)
            

