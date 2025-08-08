class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        arr = []
        i = 0
        while i < len(nums):
            s=e=i
            while e+1 < len(nums) and nums[e]+1 == nums[e+1]:
                e = e+1
            if s == e:
                arr.append(str(nums[s]))
            else:
                arr.append(str(nums[s]) + '->' + str(nums[e]))
            i = e+1
        return arr
            