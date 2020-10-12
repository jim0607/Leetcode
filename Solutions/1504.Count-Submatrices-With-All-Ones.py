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
solution 1: dp. O(M^2N)
固定以up_row为长方形上边，然后去探寻不同下边的情况,
每次探寻一个下边，我们都计算一次从up_row到down_row可能有多少个valid_submatrices,
我们把这个计算转换成一维来计算，对于每一个up_row, 都构建一个一位数组arr.  
arr[j] = 1 if from up_row to down_row, all values in column j are 1. 只要up_row到down_row有一个value is 0，
我们就设置arr[j] = 0, 表示不可能以up_row为上边以down_row为下边以j为右col构造valid submatrce.
"""
class Solution:
    def numSubmat(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        for up_row in range(m):            # 固定以up_row为长方形上边，然后去探寻不同下边的情况
            arr = [1 for _ in range(n)]    # 每次探寻一个下边，我们都计算一次从up_row到down_row可能有多少个valid_submatrices
            for down_row in range(up_row, m):
                for j in range(n):
                    if matrix[down_row][j] == 0:   #只要up_row到down_row有一个value is 0，我们就设置arr[j] = 0
                        arr[j] = 0    
                res += self._1D(arr)     # self._1D(arr) return的是以up_row为上边以down_row为下边的可能的valid submatrice的个数
                
        return res
    
    def _1D(self, arr):
        """
        Return how many subarray that are all 0s - using dp
        """
        dp = [0 for _ in range(len(arr))]   # dp[i] = how many substrings ended with arr[i]
        dp[0] = 1 if arr[0] == 1 else 0
        for i in range(1, len(arr)):
            dp[i] = dp[i-1] + 1 if arr[i] == 1 else 0
        return sum(dp)



"""
solution 2: O(MN)
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
