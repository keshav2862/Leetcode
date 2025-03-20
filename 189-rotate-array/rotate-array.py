class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        n = len(nums)
        a = n* [0]
        for i in range(n):
            a[(i + k) % n] = nums[i]
        
        for i in range(n):
            nums[i] = a[i]

