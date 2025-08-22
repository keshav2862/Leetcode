class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        l,r = 1,x
        ans = 0

        while l <= r:
            mid = l + (r - l) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
            print(ans)
        return ans