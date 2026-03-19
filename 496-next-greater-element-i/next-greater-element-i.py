class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        stack = []
        result = [-1]*n
        map1= {}
        for i,value in enumerate(nums1):
            map1[value] = i

        for i,val in enumerate(nums2):
            while stack and nums2[stack[-1]] < val:
                pop_idx = stack.pop()
                pop_val = nums2[pop_idx]
                if pop_val in map1:
                    result[map1[pop_val]] = val
            stack.append(i)
        return result