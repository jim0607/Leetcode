"""
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




"""
这道题让我们求最佳的开会地点，该地点需要到每个为1的点的曼哈顿距离之和最小，题目中给了提示，让从一维的情况来分析，先看一维时有两个点A和B的情况,

______A_____P_______B_______

可以发现，只要开会为位置P在 [A, B] 区间内，不管在哪，距离之和都是A和B之间的距离，如果P不在 [A, B] 之间，那么距离之和就会大于A和B之间的距离，现在再加两个点C和D：

______C_____A_____P_______B______D______

通过分析可以得出，P点的最佳位置就是在 [A, B] 区间内.

如果加入很多点，我们选择最佳的点是最小区间[A, B]之间的点，也就是[median - 1, median + 1]之间选一个点，

这就是为什么我们需要选择median了
"""




"""
It all about finding median, very similar with 462. Minimum Moves to Equal Array Elements II.
注意这里千万不要求mean, 而是求median
Median minimizes the absolute distance of points. 
Mean minimizes the squared distance from points.
"""
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # step 1: find row_median
        rows = []
        for i in range(m):   # 这样遍历完了之后row就已经天然sort好了，后面求meadian就很简单了
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
        row_median = rows[len(rows) // 2]
        
        # step 2: find col_median
        cols = []
        for j in range(n):  # 这样遍历完了之后col就已经天然sort好了，后面求meadian就很简单了
            for i in range(m):
                if grid[i][j] == 1:
                    cols.append(j)
        col_median = cols[len(cols) // 2]
        
        # step 3: the min total distance is sum of every house to (row_median, col_median)
        dist = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dist += abs(i - row_median) + abs(j - col_median)
        return dist
