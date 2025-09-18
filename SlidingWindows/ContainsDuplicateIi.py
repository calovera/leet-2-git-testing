/*
 * @lc app=leetcode id=1775415088 lang=python3
 *
 * ContainsDuplicateIi
 * 
 * Difficulty: Easy
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0

        windows = set()

        for right in range(0, len(nums)):
            # collapse windows
            if abs(left - right) > k:
                windows.remove(nums[left])
                left += 1
            
            if nums[right] in windows:
                return True
            windows.add(nums[right])
        return False