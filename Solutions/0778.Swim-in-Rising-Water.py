778. Swim in Rising Water

On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.



"""
find a path with the minimum max-height in the path.
采用Dikstra, 每次pop出来的都是min height就可了 - O(N^2*log(N^2)), where N is the lens of grid.
"""
from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        moves = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        hq = []
        visited = set()
        heappush(hq, (grid[0][0], (0, 0)))
        visited.add((0, 0))
        max_height = 0
        while hq:
            curr_height, curr_pos = heappop(hq)
            max_height = max(max_height, curr_height)
            if curr_pos == (n-1, n-1):
                return max_height
            
            for move in moves:
                next_x = curr_pos[0] + move[0]
                next_y = curr_pos[1] + move[1]
                if 0 <= next_x < n and 0 <= next_y < n and (next_x, next_y) not in visited:
                    heappush(hq, (grid[next_x][next_y], (next_x, next_y)))
                    visited.add((next_x, next_y))
                    
        return max_height
    
    
"""
Google 面经：有一个nxn矩阵，信使从(0, 0)出发，想走到(n-1, n-1)去报信，
中途会有一些狮子/敌营，我们离狮子的距离越远越安全，问为了尽可能到达目的地，离狮子最大的最近距离是多少？
step 1: calculate the distance of each position to the nearest lions,
put the distance information into the grid matrix.
step 2: do dikstra to find the maximum min-distance in the path,
hq stores (negative distance to lions at that pos, pos), so that each time we pop,
we pop the largest distance first, so that we keep as far as from lions as poosible.
"""
