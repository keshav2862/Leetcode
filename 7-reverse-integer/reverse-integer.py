class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x< 0:
            neg = True
            x = x*-1
        res=0
        while x>0:
            digit = x%10
            x//=10
            if (res > (2 ** 31 - 1) // 10) or (res == (2 ** 31 - 1) // 10 and digit > 7):
                return 0
            res = (res*10) + digit
        return -res if neg else res