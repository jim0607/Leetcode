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
                        
                        
"""DP solution: so brilliant
The basic idea is that doesn't mater where the destination is, we can always "rotate" the board in such a way that the knight only needs to make (1,2) or (2,1) move to approach the destination. In other words, the destination is always in the first quadrant. Except (0, 0), all other initial values in cache are the points that we have to temporarily "step out" of the first quadrant and then come back in order to reach them. Therefore, they have to be manually added at the beginning."""

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        cache = {(0, 0): 0, (1, 1): 2, (1, 0): 3, (0, 1): 3}
        
        def dp(x, y):
            if (x, y) in cache: 
                return cache[(x, y)]
            
            cache[(x, y)] = min(dp(abs(x-1), abs(y-2)), dp(abs(x-2), abs(y-1))) + 1
            
            return cache[(x, y)]
        
        return dp(abs(x), abs(y))
