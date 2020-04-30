1074. Number of Submatrices That Sum to Target

Given a matrix, and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

Example 1:

Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.


"""
用前缀和优化, 令 matrix[i][0] = matrix[i][0] + matrix[i][1] + ... + matrix[i][j], 这样matrix的行里保存的就是上面所有列的和了
然后枚举左右边界left and right, 确定左右边界left and right 之后，接下来就相当于在一列内(指的是right那一列), 求一个数组连续子串和为0的问题了
O(M*N*N)
"""
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # make a prefix sum for all rows from left to right
        # so each row is the sum of all rows before the row
        for row in matrix:
            for j in range(1, n):
                row[j] += row[j - 1]
                
        # now 枚举左右边界
        res = 0
        for left in range(n):
            for right in range(left, n):
                
                # 确定左右边界left and right 之后，接下来就相当于在一列内(指的是right那一列), 求一个数组连续子串和为0的问题了
                prefixSumCnt = collections.defaultdict(int)
                prefixSumCnt[0] = 1
                prefixSum = 0
                for row in range(m):
                    # prefixSum 需要减去左边界的和
                    prefixSum += matrix[row][right] - (matrix[row][left - 1] if left > 0 else 0)
                    
                    res += prefixSumCnt[prefixSum - target]
                    prefixSumCnt[prefixSum] += 1
        
        return res
