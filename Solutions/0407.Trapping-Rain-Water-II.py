407. Trapping Rain Water II

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.

After the rain, water is trapped between the blocks. The total volume of water trapped is 4.

"""
Recall 1D trapping water problem.  We are using the two pointers left and right, from each end of the array.
this is because that the water can only leak from left end or right end.  As long as we keep a leftMax and a righMax
to maintain the highest for left and for right, we can make sure there will be no water leak from left or right.
Here in 2D problem, we can have similar thoughts: the water can leak only from the out liners of the the 2D matrix. 
Say if we have k out liners in the matrix.  Then we can use k pointers, starting from each out liner point, just like the 
left and right pointers starting from left and right end. And we keep an array: Max[store the max height met during the 
k pointers traversal].  So the array represents the possible leak points and the height of the point.  
It is the smallest height in the array that could be the leak point.  So we only need to care about the min height in the array.
In order to access the min height in the array fast, we can use a heapq, from which getting min operation is O(1).  
So here is the algorithm:
Step 1: store all the outliners of the matrix in heapq (the four corners doesn't matter).  Maintain a visited set to mark all the visited locations.
Step 2: starting from the min height position, do BFS the 4 possible moves. If found a height < the min Height, then we can store water, else we cannot store water and we should update this leaking point by putting the new height into the heapq
Step3: in this way, we start from out liners to inside. do step 2 until heapq is empty

O(MNlogMN)
"""

"""
下面的写法稍微易懂一点
"""
class Solution:
    def trapRainWater(self, matrix: List[List[int]]) -> int:
        hq = []
        visited = set()
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m-1):
            heappush(hq, (matrix[i][0], (i, 0)))
            visited.add((i, 0))
            heappush(hq, (matrix[i][n-1], (i, n-1)))
            visited.add((i, n-1))
        for j in range(1, n-1):
            heappush(hq, (matrix[0][j], (0, j)))
            visited.add((0, j))
            heappush(hq, (matrix[m-1][j], (m-1, j)))
            visited.add((m-1, j))
            
        res = 0
        while len(hq) > 0:
            leaking_h, (i, j) = heappop(hq)
            for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_i, next_j = i + delta_i, j + delta_j
                if 0 < next_i < m - 1 and 0 < next_j < n - 1:
                    if (next_i, next_j) not in visited:
                        if matrix[next_i][next_j] < leaking_h:
                            res += leaking_h - matrix[next_i][next_j]
                            visited.add((next_i, next_j))
                            heappush(hq, (leaking_h, (next_i, next_j)))     # 注意这里是push进去(next_i, next_j)
                        else:
                            heappush(hq, (matrix[next_i][next_j], (next_i, next_j)))
                            visited.add((next_i, next_j))
        return res

"""
稍微简洁一点的写法
"""
class Solution:
    MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m == 0:
            return 0
        
        hq = []
        visited = set()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heapq.heappush(hq, (heightMap[i][j], i, j))
                    visited.add((i, j))
            
        water = 0
        while hq:
            currHeight, row, col = heapq.heappop(hq)     # currHeight is the maintained current max height from this exit, just like the leftMax in the 1D version
            
            for move in self.MOVES:
                new_row, new_col = row + move[0], col + move[1]
                
                if (new_row, new_col) not in visited and 0 <= new_row < m and 0 <= new_col < n:
                    newHeight = heightMap[new_row][new_col]
                    water += max(0, currHeight - newHeight)
                    heapq.heappush(hq, (max(currHeight, newHeight), new_row, new_col))  # remember here we push new_row, new_col even currHeight > newHeight
                    visited.add((new_row, new_col))
                        
        return water
