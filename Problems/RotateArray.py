/*
 * @lc app=leetcode id=1755119536 lang=python3
 *
 * RotateArray
 * 
 * Difficulty: Medium
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        def helper(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        start, end = 0, len(nums) - 1
        # First call to reverse the entire thing
        helper(start, end)
        
        helper(0, k-1)
        helper(k, end)




        # n = len(nums)
        # tmp = [0]*n
        # for i in range(n):
        #     tmp[ (i + k) % n] = nums[i]

        # nums[:] = tmp
        