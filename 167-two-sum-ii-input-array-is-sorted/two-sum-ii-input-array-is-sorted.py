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
        while s < e:
            flag = numbers[s] + numbers[e]
            if flag == target:
                return s+1,e+1
            else:
                if flag < target:
                    s = s+1
                else:
                    e = e-1
            