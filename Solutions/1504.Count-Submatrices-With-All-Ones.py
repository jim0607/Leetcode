"""
1504. Count Submatrices With All Ones

Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.

Example 1:

Input: mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
Example 2:

Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
Example 3:

Input: mat = [[1,1,1,1,1,1]]
Output: 21
Example 4:

Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
Output: 5
"""



"""
与84.Largest-Rectangle-in-Histogram, 85.Maximal-Rectangle很类似.
先构造histogram. 以j结尾的submatrices的个数等于heights[j] * (j - 向左找第一个height小于heights[j]的idx).
"""
class Solution:
    def numSubmat(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]  # construct the histogram 
                
        res = 0
        for i in range(m):
            res += self._histogram(matrix[i])       # helper function return the total cnt of row i
        return res
        
    def _histogram(self, heights):
        """
        算法核心是：以j结尾的submatrices的个数等于heights[j] * (j - 向左找第一个height小于heights[j]的idx)
        与84.Largest-Rectangle-in-Histogram, 85.Maximal-Rectangle很类似. we need maintain an increasing stack
        """
        cnt = [0 for _ in range(len(heights))]
        st = []
        for j, height in enumerate(heights):
            while len(st) > 0 and st[-1][0] >= height:
                st.pop()
                
            if len(st) == 0:
                cnt[j] = height * (j + 1)
            else:
                cnt[j] = height * (j - st[-1][1]) + cnt[st[-1][1]]
                
            st.append((height, j))

        return sum(cnt)
