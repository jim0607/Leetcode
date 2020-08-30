304. Range Sum Query 2D - Immutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12



"""
a 2D version prefix sum. O(1) for query.
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.presum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.presum[i+1][j+1] = self.presum[i][j+1] + matrix[i][j]

        for j in range(n):
            for i in range(m):
                self.presum[i+1][j+1] += self.presum[i+1][j]    # 这里很容易出错

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.presum[row2+1][col2+1] - self.presum[row1][col2+1] - self.presum[row2+1][col1] + self.presum[row1][col1]   # 这里很容易出错



"""
另一种不太简洁的写法
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        self.pre_sum = [[0 for _ in range(n)] for _ in range(m)]
        self.pre_sum[0][0] = matrix[0][0]
        for i in range(1, m):
            self.pre_sum[i][0] = self.pre_sum[i-1][0] + matrix[i][0]
        for j in range(1, n):
            self.pre_sum[0][j] = self.pre_sum[0][j-1] + matrix[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                self.pre_sum[i][j] = matrix[i][j] + self.pre_sum[i-1][j] + \
                self.pre_sum[i][j-1] - self.pre_sum[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.pre_sum[row2][col2]
        elif row1 == 0:
            return self.pre_sum[row2][col2] - self.pre_sum[row2][col1-1]
        elif col1 == 0:
            return self.pre_sum[row2][col2] - self.pre_sum[row1-1][col2]
        else:
            return self.pre_sum[row2][col2] - self.pre_sum[row1-1][col2] \
        - self.pre_sum[row2][col1-1] + self.pre_sum[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
