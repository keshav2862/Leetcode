class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        for i in range(32):
            a = a<<1
            a += (n&1)
            n = n>>1
        return a
        