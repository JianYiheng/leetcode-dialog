from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        if len(prices) == 1:
            return 0
        if len(prices) == 2:
            return max(prices[-1] - prices[0], 0)

        mid = int(len(prices) / 2)
        l_price = prices[0:mid]
        r_price = prices[mid + 1:]
        l_value = min(l_price)
        r_value = max(r_price)
        profit = max(r_value - l_value, r_value - prices[mid], prices[mid] - l_value)
        if profit < 0:
            profit = 0
        return max(self.maxProfit(l_price), self.maxProfit(r_price), profit)


if __name__ == "__main__":
    ret = Solution().maxProfit([7, 1, 5, 3, 6, 4])
    print(ret)
