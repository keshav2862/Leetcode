class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = 0
        e = 0
        l = 0
        ans = []
        while st<=e and e<len(s):
            if s[e] not in ans:
                ans.append(s[e]) 
                e = e + 1
                l = max(l,len(s[st:e]))
            else:
                st = st +1
                e = st
                ans = []

        return l
                
            