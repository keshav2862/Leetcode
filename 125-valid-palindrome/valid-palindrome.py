class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        news = ''.join([char for char in s if char.isalnum()])
        string1 = lower(news)
        left = 0
        right = len(string1)-1
        while left<right:
            if string1[left]==string1[right]:
                left = left+1
                right = right-1
            else:
                return False
        return True
