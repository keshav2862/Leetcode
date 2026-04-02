class Solution:
    def rob(self, nums: List[int]) -> int:
        c = nums[0]
        pc = 0
        i = 1
        while i < len(nums):
            temp = c
            c = max(pc + nums[i],c)
            pc = temp
            i = i+1
        return c