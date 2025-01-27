class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == 1 or k == 1:
            return max(nums)
        if k == len(nums):
            return float(sum(nums))/k
        s = sum(nums[:k]) 
        result = s
        for i in range(k, len(nums)):
            s += nums[i]
            s -= nums[i-k]
            print(s)
            result = max(result,s)
        return float(result)/k
            
        