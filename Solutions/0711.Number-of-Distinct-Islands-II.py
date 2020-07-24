711. Number of Distinct Islands II

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if they have the same shape, or have the same shape after rotation (90, 180, or 270 degrees only) or reflection (left/right direction or up/down direction).

Example 1:
11000
10000
00001
00011
Given the above grid map, return 1.

Notice that:
11
1
and
 1
11
are considered same island shapes. Because if we make a 180 degrees clockwise rotation on the first island, then two islands will have the same shapes.
Example 2:
11100
10001
01001
01110
Given the above grid map, return 2.

Here are the two distinct islands:
111
1
and
1
1

Notice that:
111
1
and
1
111
are considered same island shapes. Because if we flip the first array in the up/down direction, then they have the same shapes.



class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
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
                        self._transform(shape)          # 与694. Number of Distinct Islands相比就增加了这一句
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
                        
    def _trasform(self, shape):
        """
        return the transform of the shape, transform includes rotation and reflection
        """
        pass
