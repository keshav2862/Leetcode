class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        c = citations
        c.sort()
        n = len(c)
        for i in range(n):
            h = n - i 
            if c[i] >= h:
                return h
        return 0