class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        spl = s.split()
        if len(spl)!=len(pattern):
            return False
        map1 = {}
        map2 = {}

        for i in range(len(pattern)):
            c = pattern[i]
            w = spl[i]
            if c not in map1:
                map1[c] = i
            if w not in map2:
                map2[w] = i
            if map1[c] != map2[w]:
                return False

        return True