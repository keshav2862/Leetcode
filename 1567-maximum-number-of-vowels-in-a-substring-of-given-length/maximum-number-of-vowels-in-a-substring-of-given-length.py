class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {'a','e','i','o','u'}
        count = 0
        maxcount = 0
        start = 0
        for i in range(k):
                if s[i] in vowels:
                    count = count + 1
        maxcount = count
        for i in range (k,len(s)):
            if s[i-k] in vowels:
                count = count - 1
            if s[i] in vowels:
                count = count + 1
            maxcount = max(maxcount,count)
        return maxcount
