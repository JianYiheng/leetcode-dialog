from typing import List


def robs(nums: List[int], n: int) -> int:
    if n == 0:
        return nums[0]
    if n == 1:
        return max(nums[:2])
    return max(robs(nums, n - 2) + nums[n], robs(nums, n - 1))

class Solution:
    """
    遇到大数据时，会超时，递归耗时太大了
    """
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return robs(nums, len(nums)-1)


if __name__ == '__main__':
    ret = robs([1,2,3,1], 3)
    print(ret)
