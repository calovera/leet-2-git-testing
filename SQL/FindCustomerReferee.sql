/*
 * @lc app=leetcode id=1833643594 lang=mysql
 *
 * FindCustomerReferee
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE Customer.referee_id != 2 OR Customer.referee_id IS NULL;