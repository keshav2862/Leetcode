class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        r = numRows
        l = r*['']
        d = 1
        a = 0
        if r == 1:
            return s
        for i in range(len(s)):
            l[a] = l[a] + s[i]
            a= a+d
            if a == r-1:
                d = -1
            elif a == 0:
                d = 1
        return "".join(l)