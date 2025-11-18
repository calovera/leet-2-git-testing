/*
 * @lc app=leetcode id=1833648228 lang=mysql
 *
 * ArticleViewsI
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

SELECT DISTINCT author_id as id
FROM Views V
WHERE V.author_id = V.viewer_id
ORDER BY V.author_id ASC;