class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        Input: prices = [7,1,5,3,6,4]
        Output: 7
        """
        if not prices or len(prices) == 1:
            return 0

        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
