class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < (len(nums)-2):
            if nums[i] == nums[i+2]:
                nums.pop(i)
                i=i-1
            i=i+1