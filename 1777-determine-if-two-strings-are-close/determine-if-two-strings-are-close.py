class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        equal1 = {}
        equal2 = {}
        if len(word1) != len(word2):
            return False
        for x in word1:
            equal1[x] = equal1.get(x,0) + 1
        for x in word2:
            equal2[x] = equal2.get(x,0) + 1
        if set(word1) == set(word2):
            return sorted(equal1.values()) == sorted(equal2.values())
        else: 
            return False