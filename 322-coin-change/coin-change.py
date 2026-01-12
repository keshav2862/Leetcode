class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [10000000] * (amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for j in coins:
                if i-j>=0:
                    dp[i] = min(dp[i], 1+ dp[i-j])
        if dp[amount]!=10000000:
            return dp[amount]
        else: 
            return -1