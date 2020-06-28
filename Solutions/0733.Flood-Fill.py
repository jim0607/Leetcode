733. Flood Fill

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].



"""
solution 1: Union-Find
"""
class UnionFind:
    
    def __init__(self, grid):
        self.father = collections.defaultdict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.father[(i, j)] = (i, j)
                
    def find(self, x):
        if self.father[x] == x:
            return x
        
        self.father[x] = self.find(self.father[x])
        
        return self.father[x]
    
    def connected(self, a, b):
        return self.find(a) == self.find(b)
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        uf = UnionFind(image)
        
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(image), len(image[0])
        s_color = image[sr][sc]

        for i in range(m):
            for j in range(n):
                if image[i][j] == s_color:
                    for delta_i, delta_j in moves:
                        neighbor_i, neighbor_j = i + delta_i, j + delta_j
                        if 0 <= neighbor_i < m and 0 <= neighbor_j < n and image[neighbor_i][neighbor_j] == s_color:
                            uf.union((i, j), (neighbor_i, neighbor_j))
                            
        for i in range(m):
            for j in range(n):
                if image[i][j] == s_color and uf.connected((i, j), (sr, sc)):
                    image[i][j] = newColor
                        
        return image
        

"""
solution 2: bfs
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(image), len(image[0])
        s_color = image[sr][sc]
        
        q = collections.deque()
        q.append((sr, sc))
        visited = set()
        visited.add((sr, sc))
        image[sr][sc] = newColor
        
        while q:
            curr_i, curr_j = q.popleft()
            for delta_i, delta_j in moves:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and image[next_i][next_j] == s_color and \
                (next_i, next_j) not in visited:
                    visited.add((next_i, next_j))
                    q.append((next_i, next_j))
                    image[next_i][next_j] = newColor
                    
        return image
        
        
"""
solution 3: dfs iteratively 就把popleft改成pop就可以了    
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(image), len(image[0])
        s_color = image[sr][sc]
        
        q = collections.deque()
        q.append((sr, sc))
        visited = set()
        visited.add((sr, sc))
        image[sr][sc] = newColor
        
        while q:
            curr_i, curr_j = q.pop()
            for delta_i, delta_j in moves:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and image[next_i][next_j] == s_color and \
                (next_i, next_j) not in visited:
                    visited.add((next_i, next_j))
                    q.append((next_i, next_j))
                    image[next_i][next_j] = newColor
                    
        return image
        
        
"""
solution 4: dfs recurssively   
"""    
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(image), len(image[0])
        s_color = image[sr][sc]
        
        visited = set()
        visited.add((sr, sc))
        
        def dfs(curr_i, curr_j):
            image[curr_i][curr_j] = newColor
            
            for delta_i, delta_j in moves:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and image[next_i][next_j] == s_color and \
                (next_i, next_j) not in visited:
                    visited.add((next_i, next_j))
                    dfs(next_i, next_j)
                    image[next_i][next_j] = newColor
                    
        dfs(sr, sc)
        
        return image
