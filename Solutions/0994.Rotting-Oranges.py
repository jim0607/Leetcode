#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Easy (46.62%)
# Likes:    638
# Dislikes: 67
# Total Accepted:    35.6K
# Total Submissions: 76.5K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# In a given grid, each cell can have one of three values:
# 
# 
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# 
# 
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
# orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange.  If this is impossible, return -1 instead.
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
# 
# 
# 
# Example 3:
# 
# 
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the
# answer is just 0.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.
# 
# 
# 
# 
#

class Solution:
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.ROTTEN:
                    q.append((i, j))
                    
        # 层序遍历模板
        minutes = -1
        while len(q) > 0:        
            minutes += 1
            lens = len(q)
            for _ in range(lens):       
                curr_i, curr_j = q.popleft()
                for delta_i, delta_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    next_i, next_j = curr_i + delta_i, curr_j + delta_j
                    if 0 <= next_i < m and 0 <= next_j < n:
                        if grid[next_i][next_j] == self.FRESH:
                            q.append((next_i, next_j))
                            grid[next_i][next_j] = self.ROTTEN    # 就地修改grid, 所以不用visited set, 因为不会有重复访问
                            
        for i in range(m):
            for j in range(n):  
                if grid[i][j] == self.FRESH:    # 如果还有访问不到的FRESH, 那就return -1
                    return -1
                
        return 0 if minutes == -1 else minutes  # 如果minutes=-1, 那说明最开始就没有ROTTEN的进q里去
