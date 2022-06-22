class Solution:
    def maxProfit(self, prices):
        i = 0
        j = 1
        max_profit = 0
        while j < len(prices):
            curr_profit = prices[j] - prices[i]
            if prices[j] > prices[i]:
                max_profit = max(max_profit, curr_profit)
            else:
                i = j
            j += 1
        return max_profit


