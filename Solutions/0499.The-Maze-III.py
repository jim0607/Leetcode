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
    def findShortestWay(self, maze: List[List[int]], src: List[int], des: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        hq = []
        heappush(hq, (0, src[0], src[1], ""))
        visited = collections.defaultdict(tuple)
        visited[(src[0], src[1])] = 0, ""   # key is the pos visited, val is (the steps to reach there, the path to reach there)
        
        while hq:
            curr_step, curr_i, curr_j, curr_path = heappop(hq)
            
            if [curr_i, curr_j] == des:
                return curr_path    # garanteed to return the minimum step if using heapq, otherwise, not garanteed
            
            for i, j, direction in ((1,0,"d"), (-1,0,"u"), (0,1,"r"), (0,-1,"l")):
                # find the next position that the ball can stop
                next_i, next_j, next_step, next_path = curr_i, curr_j, curr_step, curr_path
                next_path += direction
                while 0 <= next_i + i < m and 0 <= next_j + j < n and maze[next_i+i][next_j+j] == self.EMPTY:
                    next_i += i
                    next_j += j
                    next_step += 1
                    if [next_i, next_j] == des:
                        break       # 注意这时不能return哦，这时not guaranted the minimum step
                                    # 因为可能这里加了很多步才到des的，只有heappop出来的才guaranteed to be minimum step
                # 这里是重点，由于bfs "一步"实际上可以走很多steps, 所以对于某个点，
                # 可能第二次到达这个点的时候所用的steps比第一次更小（甚至在第二次到达的enter方向第一次相同的情况下）
                # 所以我们不能因为第一次visited了，第二次就不去visited了，而是谁的steps少就用谁的steps
                if (next_i, next_j) not in visited or (next_step, next_path) < visited[(next_i, next_j)]:   # smallest step first, then lexicographical order
                    visited[(next_i, next_j)] = next_step, next_path
                    heappush(hq, (next_step, next_i, next_j, next_path))
        return "impossible"
