class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            print("")
        else:
            prefix = strs[0]
            for s in strs[1:]:
                while not s.startswith(prefix):
                    prefix = prefix[:-1]
                    if not prefix:
                        break
        return prefix