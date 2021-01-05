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
    
    MOVES = [(-1, 2), (1, 2), (-2, 1), (2, 1), (-1, -2), (1, -2), (-2, -1), (2, -1)]
    
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        
        x, y = abs(x), abs(y)
        
        q = collections.deque()
        visited = set()
        q.append((0, 0))
        visited.add((0, 0))
        
        step = 0
        while q:
            step += 1
            lens = len(q)
            
            for _ in range(lens):
                curr_x, curr_y = q.popleft()
                for move in self.MOVES:
                    next_x, next_y = curr_x + move[0], curr_y + move[1]
                    if (next_x, next_y) == (x, y):
                        return step
                    
                    if -2 <= next_x <= x + 2 and -2 <= next_y <= y + 2 and (next_x, next_y) not in visited:     # 这里用x >= -2 and y >= -2 pruning
                        q.append((next_x, next_y))
                        visited.add((next_x, next_y))
                        
                        
"""从source和destination两端同时进行bfs!!!!
a = {(1, 2), (3, 5)}
b = {(2, 4), (1, 2)}
print(a & b) ---> {(1, 2)}, don't know how bitwise work here, but this is how the common part was found in two sets"""
class Solution:
    MOVES = [(1, 2), (-1, -2), (2, 1), (-2, -1), (-1, 2), (1, -2), (2, -1), (-2, 1)]
    
    def minKnightMoves(self, x: int, y: int) -> int:
        self.des_x, self.des_y = abs(x), abs(y)     # 定义两个全局变量
        
        q_src, q_des = collections.deque(), collections.deque()
        visited_src, visited_des = set(), set()
        q_src.append((0, 0))
        visited_src.add((0, 0))
        q_des.append((self.des_x, self.des_y))
        visited_des.add((self.des_x, self.des_y))
        
        cnt_src, cnt_des = 0, 0
        while True:
            if visited_src & visited_des:
                return cnt_src + cnt_des
            
            q_src, visited_src = self.bfs(q_src, visited_src)
            cnt_src += 1
            
            if visited_src & visited_des:
                return cnt_src + cnt_des
            
            q_des, visited_des = self.bfs(q_des, visited_des)
            cnt_des += 1
            
    def bfs(self, q, visited):
        lens = len(q)
        for _ in range(lens):      # 层序遍历是bfs的精髓
            (x, y) = q.popleft()
            for delta_x, delta_y in self.MOVES:
                neighbor_x, neighbor_y = x + delta_x, y + delta_y
                if (neighbor_x, neighbor_y) not in visited and -2 <= neighbor_x <= self.des_x + 2 and -2 <= neighbor_y <= self.des_y + 2:
                    q.append((neighbor_x, neighbor_y))
                    visited.add((neighbor_x, neighbor_y))
       
        return q, visited
                        
                        
"""DP solution / recurssion with memorization: so brilliant
The basic idea is that doesn't mater where the destination is, we can always "rotate" the board in such 
a way that the knight only needs to make (1,2) or (2,1) move to approach the destination. 
In other words, the destination is always in the first quadrant. 
Except (0, 0), all other initial values in cache are the points that we have to temporarily "step out" 
of the first quadrant and then come back in order to reach them. 
Therefore, they have to be manually added at the beginning."""

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x = abs(x)
        y = abs(y)
        
        def backtrack(curr_x, curr_y):
            if (curr_x, curr_y) in memo:
                return memo[(curr_x, curr_y)]
        
            res = sys.maxsize
            for delta_x, delta_y in [(-1, -2), (-2, -1)]:   # 只往(0, 0)的方向走，不然会maximum resursion depth exceeded
                next_x, next_y = curr_x + delta_x, curr_y + delta_y
                next_x = abs(next_x)
                next_y = abs(next_y)
                res = min(res, 1 + backtrack(next_x, next_y))
                
            memo[(curr_x, curr_y)] = res
            return res
        
        
        memo = defaultdict(int)     # bottom up: from (x, y) --> from (x, y), minimum steps to get to (0, 0)
        memo[(0, 0)] = 0
        memo[(1, 1)] = 2
        memo[(1, 0)] = 3
        memo[(0, 1)] = 3
        return backtrack(x, y)  # returns from (x, y), minimum steps to get to (0, 0)
