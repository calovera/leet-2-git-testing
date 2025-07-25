/*
 * @lc app=leetcode id=1672068005 lang=python3
 *
 * RemoveDuplicatesFromSortedArray
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0

        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1