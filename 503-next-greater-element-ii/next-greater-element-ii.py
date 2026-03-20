class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        result = [-1]*n
        for i in range(2*n):
            idx  = i%n
            val = nums[idx]
            while stack and nums[stack[-1]] < val:
                popidx = stack.pop()
                result[popidx] = val
            stack.append(idx)
        return result
        