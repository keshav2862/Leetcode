class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expansion(s,left,right):
            while left>=0 and right < len(s) and s[left] == s[right]:
                right = right + 1
                left = left -1
            return right - left - 1
        start = 0
        end = 0
        for i in range(len(s)):
            odd = expansion(s,i,i)
            even = expansion(s,i,i+1)
            maxval = max(odd,even)

            if maxval > end - start:
                start = i - (maxval-1)//2
                end = i + maxval//2
        return s[start:end+1]
            
            

