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

# @lc code=start
class Solution:
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2
    MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        # 如果本来就没有FRESH的，就直接返回0
        found = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == self.FRESH:
                    found = True
        if not found:
            return 0        
        
        visited = set()
        minutes = self.bfs(grid, visited)  # 需要分层遍历，所以需要加入一个参数minutes

        # 判断有没有不能变质的
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == self.FRESH:
                    return -1

        return minutes - 1

    # bfs 要做的事：1. 遍历ROTTEN周边，发现FRESH就变成ROTTEN，需要层序遍历来记录需要多少minutes, 最后返回minutes
    def bfs(self, grid, visited):
        q = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == self.ROTTEN:
                    q.append((i, j))
                    visited.add((i, j)) # 一对孪生兄弟
        
        # 由于需要做层序遍历，所以要想将所有的ROTTEN都放进q （作为第一层），然后再开始q的遍历
        minutes = 0
        while q:
            lens = len(q)
            minutes += 1
            # 层序遍历
            for i in range(lens):
                (x, y) = q.popleft()
                for delta_x, delta_y in self.MOVES:
                    new_x = x + delta_x
                    new_y = y + delta_y
                    if self.isBound(new_x, new_y, grid) and grid[new_x][new_y] == self.FRESH and (new_x, new_y) not in visited:
                        grid[new_x][new_y] = self.ROTTEN
                        q.append((new_x, new_y))
                        visited.add((new_x, new_y)) # 一对孪生兄弟

        return minutes

    def isBound(self, x, y, grid):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return True
        
        return False


# @lc code=end

