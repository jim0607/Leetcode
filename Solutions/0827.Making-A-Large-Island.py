827. Making A Large Island
Hard

428

13

Add to List

Share
In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

Example 1:

Input: [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: [[1, 1], [1, 1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.


"""
solution 1: UnionFind O(MN) - 要注意每次将0变1都会改变uf的图，所以要提前用一个temp_father=uf.father来保存father的信息
"""
class UnionFind:

    def __init__(self, grid):
        self.father = collections.defaultdict()
        self.component_size = collections.defaultdict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.father[(i, j)] = (i, j)
                    self.component_size[(i, j)] = 1

    def add(self, x):
        if x not in self.father:
            self.father[x] = x
            self.component_size[x] = 1

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.component_size[root_b] += self.component_size[root_a]  # 注意顺序要与上一句对应起来


class Solution:
    def largestIsland(self, grid) -> int:
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        uf = UnionFind(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for delta_i, delta_j in moves:
                        next_i, next_j = i + delta_i, j + delta_j
                        if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]) and grid[next_i][next_j] == 1:
                            uf.union((i, j), (next_i, next_j))

        max_size = 1
        for key, val in uf.component_size.items():
            max_size = max(max_size, val)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    temp_father = uf.father.copy()  # 注意我们试探性地将(i, j)变成1试一下会改变uf这张图的，为了不改变整张图，我们保存一下uf.father, 以便可以回到之前的状态
                    temp_component_size = uf.component_size.copy()      # 注意必须用copy, 不然temp_component_size会随着uf.component_size的改变而改变，这是因为dict is mutable!
                    uf.add((i, j))
                    for delta_i, delta_j in moves:
                        next_i, next_j = i + delta_i, j + delta_j
                        if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]) and grid[next_i][next_j] == 1:
                            uf.union((i, j), (next_i, next_j))
                    max_size = max(max_size, uf.component_size[uf.find((i, j))])
                    uf.father = temp_father  # 回退回没有在图里加入(i, j)的情况，这所以可以这么做是因为UnionFind其实所有的信息都保存在self.father dict中
                    uf.component_size = temp_component_size

        return max_size
