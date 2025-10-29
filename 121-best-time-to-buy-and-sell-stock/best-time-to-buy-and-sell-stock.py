class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, sell = 0, 1
        profit = 0
        while sell < len(prices):
            if prices[sell]>prices[buy]:
                profit = max(profit, prices[sell]-prices[buy])
            else:
                buy = sell
            sell+=1
        return profit