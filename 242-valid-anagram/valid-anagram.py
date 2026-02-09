class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        freq1 = {}
        freq2 = {}
        for i in s:
            freq1[i] = freq1.get(i,0) + 1
        for i in t:
            freq2[i] = freq2.get(i,0) + 1
        if freq1 == freq2:
            return True
        return False