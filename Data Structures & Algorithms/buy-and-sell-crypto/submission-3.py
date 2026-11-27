class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0
        high = low + 1
        profit = 0
        while high < len(prices):
            if prices[high] < prices[low]:
                low = high
            else:
                profit = max(profit, prices[high]-prices[low])
            high+=1
        
        return profit