class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff = (len(prices)-1)*[0]
        i = 0
        j = 0
        maxi = 0
        while i < len(prices)-1:
            diff[i] = prices[i+1] - prices[i]
            i = i+1
        while j < len(diff):
            if diff[j] > 0:
                maxi = maxi + diff[j]
            j = j+1
        return maxi
