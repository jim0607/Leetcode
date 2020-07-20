959. Regions Cut By Slashes

In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.

 
Example 1:

Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:

Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:

Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:

Example 4:

Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:

Example 5:

Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:

 

Note:

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.





"""
Split a grid into 4 parts, each part is a uf component.
https://leetcode.com/problems/regions-cut-by-slashes/discuss/205680/JavaC%2B%2BPython-Split-4-parts-and-Union-Find
Split a cell in to 4 parts like this.
We give it a number top is 0, right is 1, bottom is 2 left is 3.
Two adjacent parts in different cells are contiguous regions.
In case '/', top and left are contiguous, botton and right are contiguous.
In case '\\', top and right are contiguous, bottom and left are contiguous.
In case ' ', all 4 parts are contiguous.
Congratulation. Now you have another problem of counting the number of islands.
"""
class UnionFind:
    
    def __init__(self):
        self.father = collections.defaultdict()
        self.cnt = 0
        
    def add(self, x):
        self.father[x] = x
        self.cnt += 1
        
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.cnt -= 1


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        uf = UnionFind()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                uf.add((i, j, 0))       # each part is a uf component
                uf.add((i, j, 1))
                uf.add((i, j, 2))
                uf.add((i, j, 3))
                if i > 0:
                    uf.union((i-1, j, 2), (i, j, 0))
                if j > 0:
                    uf.union((i, j-1, 1), (i, j, 3))
                if grid[i][j] == "\\":      # if "\", we connect 0 and 1, 2 and 3
                    uf.union((i, j, 0), (i, j, 1))
                    uf.union((i, j, 2), (i, j, 3))
                if grid[i][j] == "/":       # if "/", we connect 1 and 2, 0 and 3
                    uf.union((i, j, 1), (i, j, 2))
                    uf.union((i, j, 0), (i, j, 3))
                if grid[i][j] == " ":       # if "", we connect all 4 parts
                    uf.union((i, j, 0), (i, j, 1))
                    uf.union((i, j, 1), (i, j, 2))
                    uf.union((i, j, 2), (i, j, 3))
                    uf.union((i, j, 3), (i, j, 0))
                    
        return uf.cnt
