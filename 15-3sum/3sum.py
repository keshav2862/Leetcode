class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        
        for i, num in enumerate(nums):
            if num > 0:
                break  
            if i > 0 and num == nums[i - 1]:
                continue  
            left, right = i + 1, len(nums) - 1 
            while left < right:
                total = num + nums[left] + nums[right]
                
                if total > 0:
                    right -= 1  
                elif total < 0:
                    left += 1  
                else:
                    result.append([num, nums[left], nums[right]]) 
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return result