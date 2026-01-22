class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefsum = 0
        ans = 0
        f = {0:1}
        for i in range(len(nums)):
            prefsum = prefsum + nums[i]
            diff = prefsum - k
            ans = ans + f.get(diff,0)
            f[prefsum] = f.get(prefsum,0) + 1
        return ans