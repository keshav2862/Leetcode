class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefsum = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.prefsum[i+1] = self.prefsum[i] + nums[i]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        sumrange = self.prefsum[right+1] - self.prefsum[left]
        return sumrange


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)