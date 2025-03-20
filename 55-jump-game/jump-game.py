class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        final = len(nums)-1
        for i in range(final -1 , -1, -1):
            if nums[i] + i >= final:
                final = i
        return final == 0    

            
        