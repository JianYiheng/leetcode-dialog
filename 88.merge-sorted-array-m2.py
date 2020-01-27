from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1

        ptr, ptr1, ptr2 = len(nums1) - 1, m - 1, n - 1
        while ptr >= 0:
            if nums1[ptr1] >= nums2[ptr2]:
                nums1[ptr] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[ptr] = nums2[ptr2]
                ptr2 -= 1
            ptr -= 1
            if ptr1 < 0:
                nums1[0:ptr + 1] = nums2[0:ptr2 + 1]
                break
            if ptr2 < 0:
                break
        return nums1


if __name__ == '__main__':
    # ret = Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    ret = Solution().merge([2, 0], 1, [1], 1)
    print(ret)
