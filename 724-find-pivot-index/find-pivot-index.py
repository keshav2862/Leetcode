class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sr=sum(nums)
        sl=0
        if len(nums) ==1:
            return 0
        if len(nums) > 1:
            for i in range(len(nums)):
                if sl == sr - nums[i]:
                    return i
                sr = sr - nums[i]
                sl = sl + nums[i]
        return -1
        

        