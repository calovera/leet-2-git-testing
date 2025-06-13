/*
 * @lc app=leetcode id=1662536060 lang=python3
 *
 * ProductOfArrayExceptSelf
 * 
 * Difficulty: Medium
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)-1):
            prefix *= nums[i]
            output[i+1] = prefix
        
        suffix = 1
        for i in range(len(nums)-1,0,-1):
            suffix *= nums[i]
            output[i-1] *= suffix

        return output

        # Solution 1 (prefix and suffix sum)
        # prefix = 1
        # suffix = 1
        
        # prefixSum = []
        # suffixSum = [0]*len(nums)

        # for num in nums:
        #     prefix *= num   
        #     prefixSum.append(prefix)
        # for i in range(len(nums) - 1, -1, -1):
        #     suffix *= nums[i]
        #     suffixSum[i] = suffix
       
  
        # answer = [0]*len(nums)
        # for idx in range(len(answer)):
        #     if idx == 0:
        #         answer[idx] = suffixSum[idx + 1]
        #     elif idx == len(nums)-1:
        #         answer[idx] = prefixSum[idx - 1]
        #     else: 
        #         answer[idx] = prefixSum[idx - 1] * suffixSum[idx + 1]
        # return answer