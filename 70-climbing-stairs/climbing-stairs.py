class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=3:
            return n
        p = 3
        pp = 2
        cur = 0
        for i in range(3,n):
            cur = p + pp
            pp = p
            p = cur
        return cur