class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        absolute = []

        for i in range(len(prices)-1):

            for j in range(i+1, len(prices)):

                profit = prices[j] - prices[i]

                if profit > 0:

                    absolute.append(profit)

        if len(absolute) == 0:

            return 0

        return max(absolute)

        