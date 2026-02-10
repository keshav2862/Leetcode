class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            s = i+1
            e = n-1            
            while s < e:
                total = nums[i] + nums[s] + nums[e]
                if total == 0:
                    ans.append([nums[i],nums[s],nums[e]])
                    s = s+1
                    e = e-1
                    while s<e and nums[s] == nums[s - 1]:
                        s = s+1
                    while s < e and nums[e] == nums[e + 1]:
                        e = e-1
                elif total < 0:
                    s = s+1
                else:
                    e=e-1
        return ans
