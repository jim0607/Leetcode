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
把一个小格子斜刀分成四部分，把这四部分分别加到图中, each part is a uf component. 
如果遇到"/", 我们就把上部分和左部分连接起来, also把下部分和右部分连接起来
https://leetcode.com/problems/regions-cut-by-slashes/discuss/205680/JavaC%2B%2BPython-Split-4-parts-and-Union-Find
Split a cell in to 4 parts like this (斜刀切成四个部分).
We give it a number top is 0, right is 1, bottom is 2 left is 3.
Two adjacent parts in different cells are contiguous regions.
In case '/', top and left are contiguous, botton and right are contiguous.
In case '\\', top and right are contiguous, bottom and left are contiguous.
In case ' ', all 4 parts are contiguous.
Congratulation. Now you have another problem of counting the number of islands.
"""
class UnionFind:
    
    def __init__(self):
        self.father = collections.defaultdict(tuple)
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
        
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                uf.add((i, j, 0))   # 把一个小格子斜刀分成四部分，把这四部分分别加到图中
                uf.add((i, j, 1))   # 注意uf.add操作是包含了self.cnt+=1的
                uf.add((i, j, 2))
                uf.add((i, j, 3))
                
                if i > 0:       # 加入之后要跟上面连接起来的格子连起来
                    uf.union((i, j, 0), (i-1, j, 2))
                if j > 0:       # 也要跟左边的格子连接起来
                    uf.union((i, j, 3), (i, j-1, 1))
                    
                if grid[i][j] == "/":       # if "/", we connect part 1 and 2; also part 0 and part 3
                    uf.union((i, j, 0), (i, j, 3))
                    uf.union((i, j, 1), (i, j, 2))
                elif grid[i][j] == "\\":
                    uf.union((i, j, 0), (i, j, 1))
                    uf.union((i, j, 2), (i, j, 3))
                elif grid[i][j] == " ":
                    uf.union((i, j, 0), (i, j, 1))
                    uf.union((i, j, 1), (i, j, 2))
                    uf.union((i, j, 2), (i, j, 3))
                    uf.union((i, j, 3), (i, j, 0))
                    
        return uf.cnt
