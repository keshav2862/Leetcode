class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        else:
            fact = 1
            for i in range(1, n + 1):
                fact *= i
            return len(str(fact)) - len(str(fact).rstrip('0'))