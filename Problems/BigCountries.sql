/*
 * @lc app=leetcode id=1833646254 lang=mysql
 *
 * BigCountries
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

# Write your MySQL query statement below
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;