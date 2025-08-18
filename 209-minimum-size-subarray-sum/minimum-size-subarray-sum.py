class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        e = 0
        val = 0
        l = 10000000
        while s<=e and e<len(nums):
            if nums[e] >= target:
                return 1
            if val + nums[e] >= target:
                l = min(l, e + 1 - s)
                val -= nums[s]
                s = s + 1
            else:                        
                val += nums[e]          
                e = e + 1
        if l == 10000000:
            return 0
        return l

                    
                           

