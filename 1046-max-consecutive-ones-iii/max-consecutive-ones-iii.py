class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        count = 0
        maxcount = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                count=count+1
            while count > k:
                if nums[start] == 0:
                    count = count-1
                start = start + 1
            maxcount = max(maxcount, end - start + 1)
        return maxcount
