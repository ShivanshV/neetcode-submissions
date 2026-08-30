"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        heap = []
        for interval in intervals:
            heapq.heappush(heap,[interval.start,interval.end])
        if len(heap) == 0:
            return True
        curr = heapq.heappop(heap)
        while len(heap) != 0:
            interval = heapq.heappop(heap)
            if interval[0] < curr[1]:
                return False
            else:
                curr = interval
        return True
