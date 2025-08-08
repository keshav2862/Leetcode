class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nset = set(nums)
        lcs=0
        for num in nset:
            if num - 1 not in nset:
                l = 0
                while num + l in nset:
                    l+=1
                lcs = max(lcs,l)
        return lcs