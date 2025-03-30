class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n= len(gas)
        extra = 0
        total = 0
        start = 0
        for i in range(n):
            total += gas[i] - cost[i]
            extra += gas[i] - cost[i]
            if extra < 0:
                extra = 0
                start = i + 1
        return -1 if (total < 0) else start