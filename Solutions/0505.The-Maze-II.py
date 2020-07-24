505. The Maze II

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.

 

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.




"""
solution 1: just use a bfs, every time we reach the destination, we cannot return directly,
because第二次到达的steps可能还更小，所以我们需要记录所有达到destination所用的步数
"""
class Solution:
    EMPTY = 0
    WALL = 1
    def shortestDistance(self, maze: List[List[int]], src: List[int], des: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        hq = collections.deque()
        hq.append((0, src[0], src[1]))
        visited = collections.defaultdict(int)
        visited[(src[0], src[1])] = 0   # key is the pos visited, val is the steps to reach there
        
        min_step = float("inf")
        while hq:
            curr_step, curr_i, curr_j = hq.popleft()
            
            if [curr_i, curr_j] == des:
                min_step = min(min_step, curr_step)    # not garanteed to return the minimum step using q, so 打擂台
            
            for i, j in ((1,0), (-1,0), (0,1), (0,-1)):
                # find the next position that the ball can stop
                next_i, next_j, next_step = curr_i, curr_j, curr_step
                while 0 <= next_i + i < m and 0 <= next_j + j < n and maze[next_i+i][next_j+j] == self.EMPTY:
                    next_i += i
                    next_j += j
                    next_step += 1
                    
                # 这里是重点，由于bfs "一步"实际上可以走很多steps, 所以对于某个点，
                # 可能第二次到达这个点的时候所用的steps比第一次更小（甚至在第二次到达的enter方向第一次相同的情况下）
                # 所以我们不能因为第一次visited了，第二次就不去visited了，而是谁的steps少就用谁的steps
                if (next_i, next_j) not in visited or next_step < visited[(next_i, next_j)]:
                    visited[(next_i, next_j)] = next_step
                    hq.append((next_step, next_i, next_j))
                    
        return -1 if min_step == float("inf") else min_step



"""
solution 2: use dikstra to make sure always pop the smallest steps.  
重点是use a dictionary for visited, key is the pos visited, val is the steps to reach there.
第二次到达这个a certain pos的时候所用的steps如果比第一次更小，那就更新visited[pos].
"""
from heapq import heappush, heappop

class Solution:
    EMPTY = 0
    WALL = 1
    def shortestDistance(self, maze: List[List[int]], src: List[int], des: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        hq = []
        heappush(hq, (0, src[0], src[1]))
        visited = collections.defaultdict(int)
        visited[(src[0], src[1])] = 0   # key is the pos visited, val is the steps to reach there
        
        while hq:
            curr_step, curr_i, curr_j = heappop(hq)
            
            if [curr_i, curr_j] == des:
                return curr_step    # garanteed to return the minimum step if using heapq, otherwise, not garanteed
            
            for i, j in ((1,0), (-1,0), (0,1), (0,-1)):
                # find the next position that the ball can stop
                next_i, next_j, next_step = curr_i, curr_j, curr_step
                while 0 <= next_i + i < m and 0 <= next_j + j < n and maze[next_i+i][next_j+j] == self.EMPTY:
                    next_i += i
                    next_j += j
                    next_step += 1
                    
                # 这里是重点，由于bfs "一步"实际上可以走很多steps, 所以对于某个点，
                # 可能第二次到达这个点的时候所用的steps比第一次更小（甚至在第二次到达的enter方向第一次相同的情况下）
                # 所以我们不能因为第一次visited了，第二次就不去visited了，而是谁的steps少就用谁的steps
                if (next_i, next_j) not in visited or next_step < visited[(next_i, next_j)]:
                    visited[(next_i, next_j)] = next_step
                    heappush(hq, (next_step, next_i, next_j))
        return -1
