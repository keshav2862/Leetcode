class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        s = 0
        e = n-1
        while s<e:
            val = numbers[s] + numbers[e]
            if val == target:
                return [s+1,e+1]
            elif val < target:
                s = s+1
            else:
                e = e-1