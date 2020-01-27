from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSum = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > maxSum:
                    maxSum = profit
        return maxSum


if __name__ == "__main__":
    ret = Solution().maxProfit([7, 1, 5, 3, 6, 4])
    print(ret)
