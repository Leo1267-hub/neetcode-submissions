"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort(key = lambda i : i.start)
        pS = intervals[0].start
        pE = intervals[0].end
        for i in range(1,len(intervals)):
            s = intervals[i].start
            e = intervals[i].end
            if s < pE:
                return False
            else:
                pS,pE = s,e
        return True