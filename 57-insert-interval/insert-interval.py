class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            intervals.append(newInterval)
            return intervals
        intervals.append(newInterval)    
        intervals.sort()

        s, e = intervals[0][0], intervals[0][1]
        inter = [[s, e]]

        for i in range(1, len(intervals)):
            x = intervals[i]
            if x[0] > e:
                s = x[0]
                e = x[1]
                inter.append(x)
            else:
                e = max(e, x[1])
                inter[-1] = [s, e]
        return inter