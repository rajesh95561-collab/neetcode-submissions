class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = float("inf")
        for i in prices:
            buy = min(buy,i)
            profit = max(profit,i-buy)
        return profit