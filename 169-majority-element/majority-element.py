class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj = {}
        for i in nums:
            if i in maj:
                maj[i]=maj[i]+1
            else:
                maj[i]= 1
        res = max(maj, key=maj.get)
        return res