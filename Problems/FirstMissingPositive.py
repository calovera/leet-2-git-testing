/*
 * @lc app=leetcode id=1668806706 lang=python3
 *
 * FirstMissingPositive
 * 
 * Difficulty: Hard
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # Step 1: Clean up the array — ignore negative, 0, and out-of-range numbers
        for i in range(len(nums)):
            if(nums[i] == 0 or nums[i] < 0):
                nums[i] = len(nums) + 1


        # Step 2: Mark indices for numbers that are present
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                nums[val - 1] = -abs(nums[val - 1])
        

        # Step 3: Find the first positive index → missing number
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums)+1