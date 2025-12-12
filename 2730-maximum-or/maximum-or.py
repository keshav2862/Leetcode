class Solution(object):
    def maximumOr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        ans = 0

        pre = [0] * (n + 1)
        suf = [0] * (n + 1)

        i = 0
        while i < n:
            pre[i + 1] = pre[i] | nums[i]
            i += 1

        i = n - 1
        while i >= 0:
            suf[i] = suf[i + 1] | nums[i]
            i -= 1

        power = 1 << k  

        j = 0
        while j < n:
            value = pre[j]

            shifted = nums[j] * power  
            value = value | shifted

            value = value | suf[j + 1]  

            if value > ans:
                ans = value

            j += 1

        return ans    