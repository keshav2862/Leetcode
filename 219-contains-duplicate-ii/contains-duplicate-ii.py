class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        for i,val in enumerate(nums):
            if val in seen and i - seen[val] <= k:
                return True
            seen[val] = i
        return False