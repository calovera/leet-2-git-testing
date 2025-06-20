/*
 * @lc app=leetcode id=1670956248 lang=python3
 *
 * MergeSortedArray
 * 
 * Difficulty: Easy
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        idx = len(nums1) - 1
        first = m-1
        second = n-1

        while first >= 0 and second >= 0:

            if nums1[first] > nums2[second]:
                nums1[idx] = nums1[first]
                idx -= 1
                first -= 1
            else:
                nums1[idx] = nums2[second]
                idx -= 1
                second -= 1
        
        while first >= 0:
            nums1[idx] = nums1[first]
            idx -= 1
            first -= 1
        
        while second >= 0:
            nums1[idx] = nums2[second]
            idx -= 1
            second -= 1

        return nums1

        