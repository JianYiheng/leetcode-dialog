from typing import List


def findSide(side: bool, nums: List[int]) -> int:
    if not side:
        nums_new = reversed(nums)
    else:
        nums_new = nums
    side_sum = [0]
    for i in nums_new:
        side_sum.append(side_sum[-1] + i)
    return max(side_sum)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(max(nums), sum(nums))
        mid = int(len(nums) / 2)
        l_value = findSide(False, nums[0:mid])
        r_value = findSide(True, nums[mid + 1:])
        s_value = l_value + nums[mid] + r_value
        return max(self.maxSubArray(nums[0:mid]), s_value, self.maxSubArray(nums[mid + 1:]))


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ret = Solution().maxSubArray(nums)
    print(ret)
