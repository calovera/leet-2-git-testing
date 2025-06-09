/*
 * @lc app=leetcode id=1659110476 lang=python3
 *
 * TwoSum
 * 
 * Difficulty: Easy
 * Category: Algorithms
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i in range(0, len(nums)):
            if (target - nums[i] in values):
                return [values[target - nums[i]], i]
            else:
                values[nums[i]] = i
        return [-1,-1]