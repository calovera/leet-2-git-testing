/*
 * @lc app=leetcode id=1670883867 lang=python3
 *
 * MergeStringsAlternately
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        result = ""
        first = 0
        second = 0

        while first < n and second < m:
            result += word1[first]
            first+=1

            result +=word2[second]
            second+=1

        while first < n:
            result +=word1[first]
            first+=1

        while second < m:
            result += word2[second]
            second+=1

        return result
        