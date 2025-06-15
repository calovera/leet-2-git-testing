/*
 * @lc app=leetcode id=1665411780 lang=python3
 *
 * BestTimeToBuyAndSellStockIi
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += abs(prices[i] - prices[i-1])
        return profit