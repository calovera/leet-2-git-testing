/*
 * @lc app=leetcode id=1665335525 lang=python3
 *
 * LongestConsecutiveSequence
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        longestSequence = 0

        for num in values:
            if num - 1 not in values:  # Start of a sequence
                current = num
                currentSequence = 1

                while current + 1 in values:
                    current += 1
                    currentSequence += 1

                longestSequence = max(longestSequence, currentSequence)

        return longestSequence
