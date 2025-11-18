/*
 * @lc app=leetcode id=1833667172 lang=mysql
 *
 * ReplaceEmployeeIdWithTheUniqueIdentifier
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

SELECT EmployeeUNI.unique_id as unique_id,Employees.name
FROM Employees
LEFT JOIN EmployeeUNI
ON Employees.id = EmployeeUNI.id;