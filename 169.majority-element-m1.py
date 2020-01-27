from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        return max(count, key=lambda x: count[x])


if __name__ == '__main__':
    ret = Solution().majorityElement([3, 3, 4])
    print(ret)
