/*
 * @lc app=leetcode id=1833651099 lang=mysql
 *
 * InvalidTweets
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

# Write your MySQL query statement below
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15