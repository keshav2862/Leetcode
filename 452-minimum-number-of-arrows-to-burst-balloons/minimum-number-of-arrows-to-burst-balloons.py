class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x: x[1])
        e = points[0][1]
        a = 1
        for s,f in points:
            if s>e:
                a = a+1
                e = f
        return a