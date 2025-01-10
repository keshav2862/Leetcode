class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        i=0
        count=0
        while i < len(words):
            s = words[i:i+1]
            l =''.join(s)
            print(l)        
            l = l[0:len(pref)]
            print(l)
            if l == pref:
                count = count+1
            l=''
            i=i+1
        return count 

        