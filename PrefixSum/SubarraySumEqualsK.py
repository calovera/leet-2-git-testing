/*
 * @lc app=leetcode id=1666620491 lang=python3
 *
 * SubarraySumEqualsK
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        currentSum = 0
        prefixSums = {0 : 1}

        for num in nums:
            currentSum += num
            diff = currentSum - k

            result += prefixSums.get(diff, 0)
            prefixSums[currentSum] = 1 + prefixSums.get(currentSum, 0)


        return result