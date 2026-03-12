class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefsum = 0
        seen = {0:1}
        for i in nums:
            prefsum = prefsum + i
            count = count +  seen.get(prefsum-k,0)
            seen[prefsum] = seen.get(prefsum,0) + 1
        return count