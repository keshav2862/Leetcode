class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        for i in range(1,61):
            x = num1 - num2 * i
            if x < i:
                return -1
            if i >= bin(x).count('1'):
                return i
        return -1
