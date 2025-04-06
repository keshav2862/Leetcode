class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        rs = s[::-1]
        if rs == s:
            return True
        return False