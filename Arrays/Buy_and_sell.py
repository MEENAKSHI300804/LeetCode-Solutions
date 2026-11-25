class Solution(object):
    def maxProfit(self, prices):
        buying_price=prices[0]
        max_profit=0
        for i in range(len(prices)):
            if prices[i]<buying_price:
                buying_price=prices[i]
            else:
                current_profit = prices[i] - buying_price
                if current_profit>max_profit:
                    max_profit=current_profit
        return max_profit