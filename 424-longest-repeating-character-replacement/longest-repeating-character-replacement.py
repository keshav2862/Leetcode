class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        maxcount = 0
        charcount = {}
        ans= 0
        for right in range(len(s)):
            charcount[s[right]] = charcount.get(s[right], 0) + 1
            maxcount = max(maxcount,charcount[s[right]])
            while (right - left + 1) - maxcount > k:
                charcount[s[left]]-=1
                left = left+1
            ans = max(ans,right-left+1)
        return ans