/*
 * @lc app=leetcode id=1661465966 lang=python3
 *
 * RangeSumQuery2dImmutable
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        self.matrixSums = [[0]* (COLUMNS+1) for _ in range(ROWS+1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLUMNS):
                prefix += matrix[r][c]
                above = self.matrixSums[r][c+1]
                self.matrixSums[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1,col1 + 1,row2 + 1,col2 + 1

        region = self.matrixSums[r2][c2]
        above = self.matrixSums[r1-1][c2]
        left = self.matrixSums[r2][c1 - 1]
        topLeft = self.matrixSums[r1 - 1][c1 - 1]
        return region - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)