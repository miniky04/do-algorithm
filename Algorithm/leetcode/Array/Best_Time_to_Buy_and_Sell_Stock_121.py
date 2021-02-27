import sys


class Solution:
    def maxProfit(self, prices):
        # 시간 초과
        # max_price = 0
        #
        # for i, price in enumerate(prices):
        #     for j in range(i, len(prices)):
        #         max_price = max(prices[j] - price, max_price)
        #
        # return max_price

        # [2, 4, 1] 케이스 틀림
        # min_price = min(prices)
        # min_index = prices.index(min_price)
        #
        # if min_index == len(prices) - 1:
        #     return 0
        #
        # for n, price in enumerate(prices):
        #     if n < min_index:
        #         prices.pop(n)
        #
        # max_price = max(prices)
        #
        # return max_price - min_price

        profit = 0
        min_price = sys.maxsize
        # print("1: ", min_price)

        for price in prices:
            # print("p: ", price)
            min_price = min(min_price, price)
            # print("2: ", min_price)
            profit = max(profit, price - min_price)
            # print("3: ", profit)

        return profit


valid = Solution()
print(valid.maxProfit([2, 4, 1]))
