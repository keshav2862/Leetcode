class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, left,right):
            while left>=0 and right<len(s) and s[left] == s[right]:
                left = left -1
                right = right+1
            return (right-left-1)
        st = 0
        e = 0
        for i in range(len(s)):
            odd = expand(s,i,i)
            even = expand(s,i,i+1)
            maxval = max(odd,even)
            if maxval > e - st:
                st = i - ((maxval-1)//2)
                e = i + (maxval//2)
        return s[st:(e+1)]