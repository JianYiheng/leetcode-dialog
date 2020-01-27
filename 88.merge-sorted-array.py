from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        list2set = set(nums1+nums2)
        set2list = list(list2set)
        set2list.sort()
        nums1 = set2list
        return nums1