from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        max_sub_sum = nums[0]
        for num in nums:
            sum += num
            if sum > max_sub_sum:
                max_sub_sum = sum
            if sum < 0:
                sum = 0
        return max_sub_sum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ret = Solution().maxSubArray(nums)
    print(ret)
