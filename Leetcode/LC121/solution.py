class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        diff = [(prices[i+1]-prices[i]) for i in range(len(prices)-1)]
        for i in range(len(diff)):
            for j in range(i, len(diff)):
                returns = sum(diff[i:j+1])
                if returns > profit:
                    profit = returns
        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = prices[j]-prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            profit = price-min_price
            if profit > max_profit:
                max_profit = profit
            if min_price > price:
                min_price = price
        return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit, price-min_price)
            min_price = min(min_price, price)
        return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        max_profit = 0
        for price in prices:
            profit = price-buy
            if profit > max_profit:
                max_profit = profit
            profit = sell-price
            if profit > max_profit:
                max_profit = profit
            if buy > price:
                buy = price
            if sell < price:
                sell = price
        return max_profit


class Solution:
    def maxProfit(self, prices):
        buy = 0
        sell = 1
        max_profit = 0
        while sell < len(prices):
            currentProfit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                max_profit = max(currentProfit, max_profit)
            else:
                buy = sell
            right += 1
        return max_profit


class Solution:
    def maxProfit(self, prices):
        profit = 0
        max_profit = 0
        diffs = [prices[i+1]-prices[i] for i in range(len(prices)-1)]
        for diff in diffs:
            profit = max(0, profit+diff)
            max_profit = max(max_profit, profit)
        return max_profit


class Solution:
    def maxProfit(self, prices):
        profit = 0
        max_profit = 0
        for i in range(len(prices)-1):
            profit = max(0, profit+prices[i+1]-prices[i])
            max_profit = max(max_profit, profit)
        return max_profit


class Solution:
    def find(self, prices, i, k, buy, v):
        if k <= 0 or i >= len(prices):
            return 0
        if v[i][k] != -1:
            return v[i][k]
        if buy:
            v[i][buy] = max(-prices[i]+self.find(prices, i+1, k, not buy, v), self.find(prices, i+1, k, buy, v))
            return v[i][buy]
        else:
            v[i][buy] = max(prices[i]+self.find(prices, i+1, k-1, not buy, v), self.find(prices, i+1, k, buy, v))
            return v[i][buy]

    def maxProfit(self, prices):
        v = [[2, -1] for i in range(len(prices))]
        return self.find(prices, 0, 1, True, v)
