class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # Make it work for any order
        intervals.sort(key=lambda t: t[0])

        s, e = intervals[0][0], intervals[0][1]
        inter = [[s, e]]

        for i in range(1, len(intervals)):
            x = intervals[i]
            y = intervals[i - 1]  # kept for your original variable usage

            if x[0] > e:
                # no overlap: start a new merged block
                s = x[0]
                e = x[1]
                inter.append(x)
            else:
                # overlap: extend the end
                e = max(e, x[1])
                # update the last merged interval (instead of remove/append)
                inter[-1] = [s, e]

        return inter