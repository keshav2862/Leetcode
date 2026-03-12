class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        prevend = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            x = intervals[i]
            if x[0] >=prevend:
                prevend = x[1]
            else:
                count += 1
                prevend = min(prevend, x[1])
                
        return count