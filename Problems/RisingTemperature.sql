/*
 * @lc app=leetcode id=1834652942 lang=mysql
 *
 * RisingTemperature
 * 
 * Difficulty: Easy
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

SELECT w1.id 
FROM Weather w1
JOIN Weather w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;