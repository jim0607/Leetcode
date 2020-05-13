542. 01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]


"""
Solution 1: BFS
put all 0s into a queue, 
then pop them one by one, at the same time, change the adjacent corresponding value to be the coressponding level
"""

class Solution:
    
    ADJACENT = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return matrix
        
        m, n = len(matrix), len(matrix[0])
        
        q = collections.deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
                  
        level = 0
        while q:
            level += 1
            lens = len(q)
            
            for _ in range(len(q)):
                curr_x, curr_y = q.popleft()
                
                for delta_x, delta_y in self.ADJACENT:
                    next_x, next_y = curr_x + delta_x, curr_y + delta_y
                    
                    if 0 <= next_x < m and 0 <= next_y < n and \
                    (next_x, next_y) not in visited:
                        matrix[next_x][next_y] = level
                        q.append((next_x, next_y))
                        visited.add((next_x, next_y))
                        
        return matrix
        
        
Solution 2: DP O(MN), O(MN)

The distance of a cell from 0 can be calculated if we know the nearest distance for all the neighbours, 
in which case the distance is minimum distance of any neightbour + 1. And, instantly, the word come to mind DP!!
For each 1, the minimum path to 0 can be in any direction. So, we need to check all the 4 direction. 
In one iteration from top to bottom, we can check left and top directions, 
and we need another iteration from bottom to top to check for right and bottom direction.

Step 1: Iterate the matrix from top left to bottom right and update dp[i][j]
Step 2: Iterate the matrix from bottom right to top left and update dp[i][j]
return dp
