class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        l=[]
        count=1
        i=0
        j=0
        while j < 1:
                l.append(chars[i])
                j=j+1
        while i < len(chars)-1:
            if chars[i+1] == chars[i]:
                count=count+1
            else:
                if count > 1: 
                    l.extend(list(str(count))) 
                l.append(chars[i+1])     
            if chars[i+1] != chars[i] and count > 1:
                count = 1
            i = i+1
        if count > 1:
            l.extend(list(str(count)))
        chars[:len(l)] = l
        return len(l)
                             
        