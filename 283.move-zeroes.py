from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for ptr, num in enumerate(nums):
            if num != 0:
                nums[count] = num
                count += 1
        for ptr in range(count, len(nums)):
            nums[ptr] = 0


if __name__ == '__main__':
    x = [0, 1, 0, 3, 12]
    Solution().moveZeroes(x)
    print(x)
