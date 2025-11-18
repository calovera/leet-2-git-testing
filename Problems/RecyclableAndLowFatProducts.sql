/*
 * @lc app=leetcode id=1833641504 lang=mysql
 *
 * RecyclableAndLowFatProducts
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

# Write your MySQL query statement below
SELECT product_id 
FROM Products
WHERE low_fats = 'Y' AND recyclable='Y';