class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numap = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        a = 0
        for i in range(len(s)):
            if i+1 < len(s) and numap[s[i]] < numap[s[i + 1]]:
                a-= numap[s[i]]
            else:
                a+= numap[s[i]]
        return a   