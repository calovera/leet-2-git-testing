/*
 * @lc app=leetcode id=1665459052 lang=python3
 *
 * ValidPalindrome
 * 
 * Difficulty: Easy
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        
        return True



    # def isAlphaNumeric(ch):

    #     return (
    #         ord()
    #     )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # left, right = 0, len(s)-1

        # while left < right:
            
        #     while left < right and not s[left].isalnum():
        #         left += 1
        #     while left < right and not s[right].isalnum():
        #         right -= 1
        #     if s[left].lower() != s[right].lower():
        #         return False
        #     left += 1
        #     right -= 1

        # return True