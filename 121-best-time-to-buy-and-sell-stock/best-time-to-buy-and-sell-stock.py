class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = float('inf')
        maxprof = 0
        for i in prices:
            minprice = min(minprice,i)
            maxprof = max(maxprof,i - minprice)
        return maxprof