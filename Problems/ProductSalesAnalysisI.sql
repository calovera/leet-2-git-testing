/*
 * @lc app=leetcode id=1833671372 lang=mysql
 *
 * ProductSalesAnalysisI
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

SELECT p.product_name, s.year, s.price
FROM Product P
INNER JOIN Sales S
ON p.product_id = s.product_id;