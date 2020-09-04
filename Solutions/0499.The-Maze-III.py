499. The Maze III

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.

Given the ball position, the hole position and the maze, find out how the ball could drop into the hole by moving the shortest distance. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the hole (included). Output the moving directions by using 'u', 'd', 'l' and 'r'. Since there could be several different shortest ways, you should output the lexicographically smallest way. If the ball cannot reach the hole, output "impossible".

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The ball and the hole coordinates are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (0, 1)

Output: "lul"

Explanation: There are two shortest ways for the ball to drop into the hole.
The first way is left -> up -> left, represented by "lul".
The second way is up -> left, represented by 'ul'.
Both ways have shortest distance 6, but the first way is lexicographically smaller because 'l' < 'u'. So the output is "lul".

Example 2:

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (3, 0)

Output: "impossible"

Explanation: The ball cannot reach the hole.

 

Note:

There is only one ball and one hole in the maze.
Both the ball and hole exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and the width and the height of the maze won't exceed 30.


class Solution:
    EMPTY = 0
    WALL = 1
    def findShortestWay(self, grid: List[List[int]], src: List[int], destination: List[int]) -> str:
        m, n = len(grid), len(grid[0])
        hq = [(0, src[0], src[1], "")]
        distance = collections.defaultdict(tuple)
        distance[(src[0], src[1])] = (0, "")    # key is the pos visited, val is (the dist to reach there, the path to reach there)
        while len(hq) > 0:
            curr_dist, curr_i, curr_j, curr_path = heappop(hq)
            if [curr_i, curr_j] == destination:
                return curr_path        # garanteed to return the minimum step if using heapq, otherwise, not garanteed
            
            for delta_i, delta_j, direction in [(0, 1, "r"), (1, 0, "d"), (-1, 0, "u"), (0, -1, "l")]:
                next_i, next_j = curr_i, curr_j
                next_steps = 0
                while 0 <= next_i + delta_i < m and 0 <= next_j + delta_j < n and grid[next_i + delta_i][next_j + delta_j] == self.EMPTY:
                    next_i += delta_i
                    next_j += delta_j
                    next_steps += 1
                    if [next_i, next_j] == destination:  # 注意跟maze II不一样的是足球可以在半路掉进洞的, 即destination is not a stoppable node
                        break   # 注意这时不能return哦，这时not guaranted the minimum step, 因为可能这里加了很多很多步才到des的，
                                # 只有heappop出来的才guaranteed to be minimum step
                       
                next_dist = curr_dist + next_steps
                next_path = curr_path + direction
                if (next_i, next_j) not in distance or (next_dist, next_path) < distance[(next_i, next_j)]: # smallest step first, then lexicographical order
                    distance[(next_i, next_j)] = (next_dist, next_path)
                    heappush(hq, (next_dist, next_i, next_j, next_path))
                    
        return "impossible"
