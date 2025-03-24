class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = nums[0]
        pc = 0
        i = 1
        li = 0
        while i < len(nums):
            t = c
            c = max(c,pc + nums[i])
            pc = t
            i = i + 1
        return c