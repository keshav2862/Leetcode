class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        x= 0
        if n == 1:
            return [0]
        if n == 0:
            return []
        l = []
        if n % 2 != 0:
            l.append(0)
        for i in range(n//2):
            x = x + 1
            l.append(x)
            l.append(-x)
        if len(l) == n:
            return l
        