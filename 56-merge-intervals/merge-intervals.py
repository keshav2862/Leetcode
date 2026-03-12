class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        intervals.sort()
        s = intervals[0][0]
        e = intervals[0][1]
        res = [[s,e]]

        for i in range(1,len(intervals)):
            a = intervals[i]
            if a[0] > e:
                s = a[0]
                e = a[1]
                res.append([s,e])
            else:
                e = max(e,a[1])
                res[-1] = [s,e]
        return res