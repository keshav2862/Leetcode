class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini = prices[0]
        maxi = 0
        for i in prices[1:]:
           maxi = max(maxi, i - mini)
           mini = min(mini, i)
        return maxi 
