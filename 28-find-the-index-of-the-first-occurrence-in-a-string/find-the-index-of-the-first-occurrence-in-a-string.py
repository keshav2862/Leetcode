class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        if needle == haystack:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+n] == needle:
                return i
        return -1
            