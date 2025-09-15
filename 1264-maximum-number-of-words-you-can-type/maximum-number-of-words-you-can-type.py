class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        w = text.split(' ')
        l = list(brokenLetters)
        n = []
        flag = 0
        print(l,w)
        for x in w:
            for a in l:
                if a in x:
                    break
            else:
                flag = flag + 1
        return flag

