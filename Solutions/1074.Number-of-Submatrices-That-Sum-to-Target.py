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
solution 2: same idea O(M*M*N)
也可以先把行处理好，让每一行里面保存上面所有行的和
接下来就是在每一行里面去求560问题了，注意一点不同的是需要遍历upRow和downRow的, 如果不遍历就是solution 3的错误写法
举一个反例想明白solution 3为什么行不通，自然就会改成solution 2了
"""   
"""
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for row in range(1, m):
            for col in range(n):
                matrix[row][col] += matrix[row - 1][col]
            
        cnt = 0
        for upRow in range(m):
            for downRow in range(upRow, m):
                prefixSumDict = collections.defaultdict(int)
                prefixSumDict[0] = 1
                prefixSum = 0
                for col in range(n):
                    prefixSum += matrix[downRow][col] - (matrix[upRow-1][col] if upRow >= 1 else 0)
                    if prefixSum - target in prefixSumDict:
                        cnt += prefixSumDict[prefixSum - target]
                    prefixSumDict[prefixSum] += 1
                
        return cnt


    
"""
solution 3: 行不通的solution: 让每一行里面保存上面所有行的和， 接下来就是在每一行里面去求560问题了
举一个反例想明白solution 3为什么行不通，自然就会改成solution 2了
反例: [[5, 1], [1, 5]], 如果简单地认为不用遍历upRow和downRow，那就会丢掉下面一行[1, 5]的信息，从而输出3而不是4
"""   
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for row in range(1, m):
            for col in range(n):
                matrix[row][col] += matrix[row - 1][col]
            
        # 下面与560一模一样
        cnt = 0
        for row in range(m):
            prefixSumDict = collections.defaultdict(int)
            prefixSumDict[0] = 1
            prefixSum = 0
            for num in matrix[row]:
                prefixSum += num
                if prefixSum - target in prefixSumDict:
                    cnt += prefixSumDict[prefixSum - target]
                prefixSumDict[prefixSum] += 1
                
        return cnt
    
    
    
    
    
    
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
