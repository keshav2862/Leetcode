class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final = len(nums)-1
        count = 0
        val = 0
        end = 0
        if len(nums) == 1:
            return 0
        for i in range(final):
            val = max(val,i+nums[i])
            if i == end:
                count = count + 1
                end = val
                if end>=final:
                    return count
        return count