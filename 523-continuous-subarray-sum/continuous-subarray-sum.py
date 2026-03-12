class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <2:
            return False
        prefsum = 0
        seen = {0:-1}
        for i,num in enumerate(nums):
            prefsum = prefsum + num
            rem = prefsum % k
            if rem in seen:
                if i - seen[rem] >= 2:
                    return True
            else:
                seen[rem] = i
        return False