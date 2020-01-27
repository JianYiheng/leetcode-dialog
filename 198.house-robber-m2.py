from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev = nums[0]
        curr = max(nums[:2])
        for i in nums[2:]:
            curr, prev = max(prev + i, curr), curr
        return curr


if __name__=='__main__':
    ret = Solution().rob([2, 7, 9, 19, 3, 1])
    print(ret)
