/*
 * @lc app=leetcode id=1775378617 lang=python3
 *
 * BoatsToSavePeople
 * 
 * Difficulty: Medium
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        boats = 0
        left = 0
        right = len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                boats += 1
            else:
                right -= 1
                boats += 1

        return boats