"""
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
"""


"""
step 1: use the relative lacation of each "1" with respect to the staring point as the signature of shape.
step 2: rotate and reflect+rotate them against (0,0) in 8 directions, to get hte signature of the rotated shapes
step 3: choose the smallest among 8 directions to hash.
"""
class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
   
        # step 1: use the relative lacation of each "1" with respect to the staring point as the signature of shape.
        def dfs(org_i, org_j, curr_i, curr_j):
            shape.append([curr_i - org_i, curr_j - org_j])      # append the relative lacation into shape
            for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if grid[next_i][next_j] == 1:
                        if (next_i, next_j) not in visited:
                            visited.add((next_i, next_j))
                            dfs(org_i, org_j, next_i, next_j)
                            
        # step 2: rotate and reflect+rotate them against (0,0) in 8 directions, to get hte signature of all the rotated shapes         
        def rotate(shape):
            rotated = [[] for _ in range(8)]
            for x, y in shape:
                rotated[0].append([x, y])
                rotated[1].append([-x, y])
                rotated[2].append([x, -y])
                rotated[3].append([-x, -y])
                rotated[4].append([y, x])
                rotated[5].append([-y, x])
                rotated[6].append([y, -x])
                rotated[7].append([-y, -x])
            for rot in rotated:
                rot.sort()
                x0, y0 = rot[0]
                for pos in rot:
                    pos[0] -= x0
                    pos[1] -= y0
            rotated.sort()
            return rotated[0]       # rotated[0] is the signature of the rotated shapes now
                            
        
        shapes = set()
        visited = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    shape = []
                    visited.add((i, j))
                    dfs(i, j, i, j)                 # pass original_i and original_j into dfs
                    rotated_shape = rotate(shape)   # get the signature of the shape
                    shapes.add(tuple(x for pos in rotated_shape for x in pos))

        return len(set(shapes))
