/*
 * @lc app=leetcode id=1750657563 lang=python3
 *
 * 4sum
 * 
 * Difficulty: Medium
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        res, quad = [],[]

        def kSum(k, start, target):
            if k == 2:

                # Implement Two Sum
                left, right = start, len(nums)-1
                while left < right:
                    if nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[left] + nums[right] < target:
                        left += 1
                    else:
                        res.append(quad + [nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                return
            
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i-1]:
                    continue
                quad.append(nums[i])
                kSum(k-1, i + 1, target - nums[i])
                quad.pop()
        kSum(4, 0, target)
        return res
