/*
 * @lc app=leetcode id=1675596659 lang=python3
 *
 * 3sum
 * 
 * Difficulty: Medium
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)-2):

            left = i + 1
            right = len(nums)-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1
        
        return result
                