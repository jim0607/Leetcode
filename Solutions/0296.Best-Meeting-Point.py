296. Best Meeting Point

A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

Input: 

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6 

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance 
             of 2+2+2=6 is minimal. So return 6.


"""
It all about finding median, very similar with 462. Minimum Moves to Equal Array Elements II
"""
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = []
        col = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row.append(i)     # 这样遍历完了之后row就已经天然sort好了，后面求meadian就很简单了
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    col.append(j)     # 这样遍历完了之后col就已经天然sort好了，后面求meadian就很简单了

        # 注意这里千万不要求mean, 而是求median
        # Median minimizes the absolute distance of points. 
        # Mean minimizes the squared distance from points.
        row_median = row[len(row)//2]
        col_median = col[len(col)//2]

        dist = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dist += abs(i - row_median) + abs(j - col_median)
        return dist
