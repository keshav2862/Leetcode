class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        curmax = nums[0]
        maxglobal = nums[0]
        curmin = nums[0]
        minglobal = nums[0]
        total = sum(nums)
        for i in range(1,len(nums)):
            curmax = max(nums[i],curmax+nums[i])
            maxglobal = max(curmax,maxglobal)
            curmin = min(nums[i],curmin+nums[i])
            minglobal = min(curmin,minglobal)
        if maxglobal<0:
            return maxglobal
        return max(maxglobal,total - minglobal)