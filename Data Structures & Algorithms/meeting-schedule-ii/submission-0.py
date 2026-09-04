"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start,end = [],[]
        for intr in intervals:
            start.append(intr.start)
            end.append(intr.end)
        start.sort()
        end.sort()
        res,cur = 0,0
        s,e = 0,0
        while s < len(start):
            if start[s] < end[e]:
                cur += 1
                s += 1
                res = max(res,cur)
            else:
                cur -= 1
                e += 1
        return res