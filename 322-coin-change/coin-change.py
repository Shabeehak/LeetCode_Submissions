class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[amount+1]*int(amount+1) #creating a array from 0 to amount index with a higher value of amount as value
        dp[0]=0
        for value in range(1, amount+1):
            for coin in coins:
                if value-coin>=0:
                    dp[value]=min(dp[value], 1 + dp[value-coin])
        return dp[amount] if dp[amount]!=amount+1 else -1