/*
 * @lc app=leetcode id=1659145335 lang=javascript
 *
 * TwoSum
 * 
 * Difficulty: Easy
 * Category: Algorithms
 * Runtime: N/A
 * Memory: N/A
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map();

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];

        if (map.has(complement)) {
            return [map.get(complement), i];
        }

        map.set(nums[i], i);
    }

    return []; // in case no solution found
};
