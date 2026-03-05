class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        ans = 0
        rec = set()
        ls = list(s)
        for right in range(len(ls)):
            while s[right] in rec:
                rec.remove(s[left])
                left += 1
            rec.add(s[right])
            ans = max(ans,len(rec))
        return ans


                
            