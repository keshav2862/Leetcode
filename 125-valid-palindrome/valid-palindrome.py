import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cs = re.sub(r'[^a-zA-Z0-9]', '', s)
        print cs
        cs = cs.lower()
        rs = cs[::-1]

        
        if cs == rs:
            return True
        return False