class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numap ={}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numap:
                return [i,numap[complement]]
            numap[nums[i]] = i