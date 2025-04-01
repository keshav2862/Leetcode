class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        print(strs[0])
        a = strs[0]
        l = len(strs[0])
        for i in range(n):
            while not strs[i].startswith(a):
                a = a[:-1]
                if not a:
                    break
        return a