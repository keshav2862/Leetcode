class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l1 = [1]*n
        l2 = [1]*n

        for i in range(1,n):
            l1[i] = l1[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            l2[i] = l2[i+1]*nums[i+1]
        for i in range(n):
            l2[i] = l1[i]*l2[i]
        return l2