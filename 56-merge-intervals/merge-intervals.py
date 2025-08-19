class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        intervals.sort()

        s, e = intervals[0][0], intervals[0][1]
        inter = [[s, e]]

        for i in range(1, len(intervals)):
            x = intervals[i]
            y = intervals[i - 1] 

            if x[0] > e:
                s = x[0]
                e = x[1]
                inter.append(x)
            else:
                e = max(e, x[1])
                inter[-1] = [s, e]

        return inter