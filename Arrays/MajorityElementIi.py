/*
 * @lc app=leetcode id=1665444879 lang=python3
 *
 * MajorityElementIi
 * 
 * Difficulty: Medium
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = Counter(nums)

        result = []

        for num, counter in freq.items():
            if counter > n//3:
                result.append(num)
        return result
        