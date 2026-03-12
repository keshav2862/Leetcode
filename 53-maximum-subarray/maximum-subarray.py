class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        curmax = nums[0]
        endcur = nums[0]
        for i in range(1,len(nums)):
            endcur = max(nums[i],endcur+nums[i])
            curmax = max(curmax,endcur)
        return curmax