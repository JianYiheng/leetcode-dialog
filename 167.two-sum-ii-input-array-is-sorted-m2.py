from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = {}
        for index, num in enumerate(numbers):
            if target - num not in visited:
                visited[num] = index + 1
            else:
                return [visited[target-num], index + 1]


if __name__ == '__main__':
    ret = Solution().twoSum([2,7,11,15], 9)
    print(ret)
