class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax = nums[0]
        curmin = nums[0]
        result = nums[0]
        for n in nums[1:]:
            candidates = (n, n*curmax, n*curmin)
            curmax = max(candidates)
            curmin = min(candidates)
            result = max(result, curmax)
        return result        