from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (not prices) | len(prices) == 1:
            return 0
        #prices = list(map(float, prices))
        prices.insert(0, float('inf'))
        prices.append(-float('inf'))

        min_price = 0
        profit_sum = 0
        flag = False

        for i in range(1, len(prices)-1):
            if (prices[i] <= prices[i+1]) & (prices[i] <= prices[i-1]) & (not flag):
                min_price = prices[i]
                flag = True
            if (prices[i] >= prices[i+1]) & (prices[i] >= prices[i-1]) & flag:
                profit_sum += prices[i] - min_price
                flag = False
            print('min_price: ', min_price)
        return int(profit_sum)


if __name__ == "__main__":
    ret = Solution().maxProfit([2, 2, 5])
    print(ret)
