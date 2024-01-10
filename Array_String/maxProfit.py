class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        Input: prices = [7,1,5,3,6,4]
        Output: 5
        """
        if not prices or len(prices) == 1:
            return 0

        low, maxDiff = prices[0], 0
        for price in prices[1:]:
            if price < low:
                low = price
            else:
                diff = price - low
                if diff > maxDiff:
                    maxDiff = diff
        return maxDiff
        
        
