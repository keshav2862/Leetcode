class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = 0
        i=0
        j=0
        while i < len(s):
            while j < len(t):
                if s[i] == t[j]:
                    count = count + 1
                    flag = j
                    print(flag)    
                    break             
                j = j+1
                # if count>0:
                #     print(flag)
            i = i+1
            if count > 0:
                j = flag + 1 
        # print(count)
        if count == len(s):
            return True
        return False