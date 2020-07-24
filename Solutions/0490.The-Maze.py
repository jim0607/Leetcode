490. The Maze

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

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

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false

"""
像1263. Minimum Moves to Move a Box to Their Target Location那道题一样, 
bfs need to pass direction into the q, so that we know where the ball is coming from
"""
class Solution:
    EMPTY = 0
    WALL = 1
    def hasPath(self, maze: List[List[int]], src: List[int], des: List[int]) -> bool:
        # modify maze
        m, n = len(maze), len(maze[0])
        modified_maze = [[1 for _ in range(n+2)] for _ in range(m+2)]
        for i in range(m):
            for j in range(n):
                modified_maze[i+1][j+1] = maze[i][j] 
        maze = modified_maze
        m += 2
        n += 2
        src = (src[0] + 1, src[1] + 1)
        des = (des[0] + 1, des[1] + 1)
        
        # edge case: if the des 的四周没有墙那就停不住，如果四面都是墙那就进不来
        # 如果上下两面是墙，左右两面都是通的，那也停不住
        moves = collections.defaultdict(tuple)
        moves["right"] = (1, 0)
        moves["left"] = (-1, 0)
        moves["up"] = (0, 1)
        moves["down"] = (0, -1)
        if all(maze[des[0]+move[0]][des[1]+move[1]] == self.EMPTY for move in moves.values()):
            return False
        if all(maze[des[0]+move[0]][des[1]+move[1]] == self.WALL for move in moves.values()):
            return False
        if maze[des[0]+moves["right"][0]][des[1]+moves["right"][1]] == self.EMPTY and \
        maze[des[0]+moves["left"][0]][des[1]+moves["left"][1]] == self.EMPTY and \
        maze[des[0]+moves["up"][0]][des[1]+moves["up"][1]] == self.WALL and \
        maze[des[0]+moves["down"][0]][des[1]+moves["down"][1]] == self.WALL:
            return False
        if maze[des[0]+moves["right"][0]][des[1]+moves["right"][1]] == self.WALL and \
        maze[des[0]+moves["left"][0]][des[1]+moves["left"][1]] == self.WALL and \
        maze[des[0]+moves["up"][0]][des[1]+moves["up"][1]] == self.EMPTY and \
        maze[des[0]+moves["down"][0]][des[1]+moves["down"][1]] == self.EMPTY:
            return False
        
        # bfs, need to pass direction into the q, so that we know where the ball is coming from
        q = collections.deque()
        visited = set()
        for direction, move in moves.items():
            if maze[src[0]+move[0]][src[1]+move[1]] == self.EMPTY:
                q.append((src[0], src[1], direction))     # put direction into q
                visited.add((src[0], src[1], direction))
                
        while q:
            curr_i, curr_j, curr_dir = q.popleft()
            next_i, next_j = curr_i + moves[curr_dir][0], curr_j + moves[curr_dir][1]
            while maze[next_i][next_j] == self.EMPTY:  # cannot stop at an empty place, must stop at wall
                curr_i += moves[curr_dir][0]
                curr_j += moves[curr_dir][1]
                next_i += moves[curr_dir][0]
                next_j += moves[curr_dir][1]
                
            # now that curr_i, curr_j stopped at wall, we can choose which direction to go next
            # before that, let's check if curr stopped pos is the destination
            if (curr_i, curr_j) == des:
                return True
            
            for next_dir, next_move in moves.items():
                next_i, next_j = curr_i + next_move[0], curr_j + next_move[1]
                if maze[next_i][next_j] == self.WALL:
                    continue
                if (next_i, next_j, next_dir) in visited:
                    continue
                q.append((next_i, next_j, next_dir))     # put direction into q
                visited.add((next_i, next_j, next_dir))
            
        return False
