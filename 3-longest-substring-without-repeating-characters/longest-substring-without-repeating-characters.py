class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = 0
        e = 0
        l = 0
        ans = set()
        while st<=e and e<len(s):
            if s[e] not in ans:
                ans.add(s[e]) 
                l = max(l,e-st+1)
                e = e + 1
            else:
                ans.remove(s[st])
                st = st+1
        return l
                
            