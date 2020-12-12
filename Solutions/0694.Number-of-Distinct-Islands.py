"""
694. Number of Distinct Islands

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
"""

"""
solution 2: use the relative lacation of each "1" with respect to the staring point as the signature of shape.
"""
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(org_i, org_j, curr_i, curr_j):
            shape.append((curr_i - org_i, curr_j - org_j))      # append the relative lacation into shape
            for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if grid[next_i][next_j] == 1:
                        if (next_i, next_j) not in visited:
                            visited.add((next_i, next_j))
                            dfs(org_i, org_j, next_i, next_j)
                            
        
        shapes = []
        visited = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    shape = []
                    visited.add((i, j))
                    dfs(i, j, i, j)         # pass original_i and original_j into dfs
                    shapes.append(tuple(shape))
        return len(set(shapes))
       


"""
When we start a dfs on the top-left square of some island, the path taken by dfs will be the same
if and only if the shape is the same. So path is the signature of shape.
So we can record the path, and count how many distinct path.
"""
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(curr_i, curr_j, curr_dir):
            shape.append(curr_dir)      # append path into shape
            for delta_i, delta_j, next_dir in [(1, 0, "d"), (-1, 0, "u"), (0, 1, "r"), (0, -1, "l")]:  # 把方向信息也要带进去
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if grid[next_i][next_j] == 1:
                        if (next_i, next_j) not in visited:
                            visited.add((next_i, next_j))
                            dfs(next_i, next_j, next_dir)
                            shape.append("b")   # for loop 走完了加上"b", to mark the end of a path
                                                # 非常重要！！下面举例讲解
        
        shapes = []
        visited = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    shape = []
                    visited.add((i, j))
                    dfs(i, j, "")
                    shapes.append("".join(shape))
        return len(set(shapes))

"""
[[1,1,0],
 [0,1,1],
 [0,0,0],
 [1,1,1],
 [0,1,0]]
如果没有最后一句go back, 那么shapes = ['rdr', 'rdr'], 错误认为两种shape相同
加了最后一句go back就不一样了，会在走不下去的时候加上b, 此时的shapes = ['rdrbbb', 'rdbrbb'].
注意这里的输出要想清楚，面试肯定会问到的
"""
              
""" 
folow up: note that we can also use the relative locations of each "1" 
with respect to the starting point as the signature of shape 
"""



class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.moves = [(1,0,"d"), (0,1,"r"), (-1,0,"u"), (0,-1,"l")]     # 把方向信息也要带进去
        shapes = []
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if (i, j) not in visited:
                        visited.add((i, j))
                        shape = []
                        self._dfs(grid, i, j, visited, "o", shape)      # "o" means original point
                        shapes.append("".join(shape))
                        
        return len(set(shapes))
        
    def _dfs(self, grid, i, j, visited, direction, shape):
        shape.append(direction)
        
        for delta_i, delta_j, next_dir in self.moves:
            next_i, next_j = i + delta_i, j + delta_j
            if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]):
                if grid[next_i][next_j] == 1:
                    if (next_i, next_j) not in visited:
                        visited.add((next_i, next_j))
                        self._dfs(grid, next_i, next_j, visited, next_dir, shape)
                        shape.append("b")       # go back 非常重要！！下面举例讲解
        

