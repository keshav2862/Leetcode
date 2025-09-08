class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def hasZero(x):
            return '0' in str(x)
        for i in range(n):
            a = i
            b = n-i
            if not hasZero(a) and not hasZero(b):
                return [a,b]
            