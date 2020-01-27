from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptrl, ptrr = 0, len(numbers)-1
        while numbers[ptrl] + numbers[ptrr] != target:
            if numbers[ptrl] + numbers[ptrr] > target:
                ptrr -= 1
            elif numbers[ptrl] + numbers[ptrr] < target:
                ptrl += 1
            if ptrl == ptrr:
                return []
        return [ptrl+1, ptrr+1]


if __name__ == '__main__':
    ret = Solution().twoSum([-1, 0], -1)
    print(ret)