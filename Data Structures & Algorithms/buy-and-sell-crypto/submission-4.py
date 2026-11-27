class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        high = 0
        profit = 0
        while high < len(prices):
            if prices[high] < low:
                low = prices[high]
            else:
                profit = max(profit, prices[high]-low)
            high+=1
        
        return profit