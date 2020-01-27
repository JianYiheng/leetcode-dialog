from typing import List


class Solution:
    """
    这个算法必须在 数列一定有众数的情况下 才能实现
    """
    def majorityElement(self, nums: List[int]) -> int:
        count, majority = 1, nums[0]
        for num in nums[1:]:
            if count == 0:
                majority = num
            if num == majority:
                count += 1
            else:
                count -= 1
        return majority


if __name__ == '__main__':
    ret = Solution().majorityElement([7, 7, 5, 7, 5, 5])
    print(ret)
