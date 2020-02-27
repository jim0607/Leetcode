#
# @lc app=leetcode id=1197 lang=python3
#
# [1197] Minimum Knight Moves
#
# https://leetcode.com/problems/minimum-knight-moves/description/
#
# algorithms
# Medium (31.64%)
# Likes:    88
# Dislikes: 35
# Total Accepted:    7.9K
# Total Submissions: 24.7K
# Testcase Example:  '2\n1'
#
# In an infinite chess board with coordinates from -infinity to +infinity, you
# have a knight at square [0, 0].
# 
# A knight has 8 possible moves it can make, as illustrated below. Each move is
# two squares in a cardinal direction, then one square in an orthogonal
# direction.
# 
# 
# 
# Return the minimum number of steps needed to move the knight to the square
# [x, y].  It is guaranteed the answer exists.
# 
# 
# Example 1:
# 
# 
# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]
# 
# 
# Example 2:
# 
# 
# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
# 
# 
# 
# Constraints:
# 
# 
# |x| + |y| <= 300
# 
# 
#

"""简单图的最短路径问题，一看就是层序遍历的BFS"""

# @lc code=start
class Solution:
    MOVES = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    def minKnightMoves(self, x: int, y: int) -> int:
        if (x, y) == (0, 0):
            return 0

        visited = set()
        steps = self.bfs(x, y, visited)

        return steps

    # bsf 层序遍历，输出层数
    def bfs(self, x, y, visited):
        steps = 0
        q = collections.deque()
        q.append((0, 0))
        visited.add((0, 0))     # 一对孪生兄弟
        # 第76-83行是固定必须背诵的
        while q:
            lens = len(q)   # 层序遍历必备句式1
            steps += 1      # 层序遍历必备句式2
            for _ in range(lens):   # 层序遍历必备句式之最重要
                (curr_x, curr_y) = q.popleft()    # 层序遍历必备句式4
                for delta_x, delta_y in self.MOVES:   # 层序遍历必备句式3
                    new_x = curr_x + delta_x          # 层序遍历必备句式5
                    new_y = curr_y + delta_y          # 层序遍历必备句式6
                    if (new_x, new_y) == (x, y):
                        return steps
                    if (new_x, new_y) not in visited:
                        q.append((new_x, new_y))
                        visited.add((new_x, new_y))     # 孪生兄弟

        
# @lc code=end


# 为了解决TLE问题，尝试利用对称性质: x, y = abs(x), abs(y); append neighbor to q only if (neighbor_x >= -2 and neighbor_y >= -2)
class Solution:
    MOVES = [(1, 2), (-1, -2), (2, 1), (-2, -1), (-1, 2), (1, -2), (2, -1), (-2, 1)]
    
    def minKnightMoves(self, x: int, y: int) -> int:
        if (x, y) == (0, 0):
            return 0
        
        x, y = abs(x), abs(y)
        steps = self.bfs(x, y)
        
        return steps
    
    def bfs(self, destination_x, destination_y):
        """bfs the board layer by layer to find the layer number of (x, y), return the layer number"""
        q = collections.deque()
        visited = set()
        q.append((0, 0))
        visited.add((0, 0))
        
        steps = 0
        while q:
            steps += 1
            lens = len(q)
            for _ in range(lens):
                (x, y) = q.popleft()
                for delta_x, delta_y in self.MOVES:
                    neighbor_x, neighbor_y = x + delta_x, y + delta_y
                    if (neighbor_x, neighbor_y) == (destination_x, destination_y):
                        return steps
                    if (neighbor_x, neighbor_y) not in visited and (neighbor_x >= -2 and neighbor_y >= -2):
                        q.append((neighbor_x, neighbor_y))
                        visited.add((neighbor_x, neighbor_y))
