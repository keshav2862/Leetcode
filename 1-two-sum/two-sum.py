class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in x:
                return[i,x[c]]
            x[nums[i]] = i