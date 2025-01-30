class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        start = 0
        end = len(nums) - 1
        i = 0
        count = 0
        while start < end:
            if nums[start] + nums[end] == k:
                count+=1
                start = start +1
                end=end-1
            elif nums[start] + nums[end] > k:
                end = end - 1
            else:
                start = start +1
        return count
        