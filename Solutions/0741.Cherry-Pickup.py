"""
741. Cherry Pickup

In a N x N grid representing a field of cherries, each cell is one of three possible integers.


0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.

Your task is to collect maximum number of cherries possible by following the rules below:


Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.
 

Example 1:

Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation: 
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
"""


"""
Fisrt of all, we cannot find max for trip (0, 0) -> (n-1, n-1), then find max for trip (n-1, n-1) -> (0, 0).
This is wrong because https://www.cnblogs.com/grandyang/p/8215787.html
"""
"""
Go from (0, 0) -> (n-1, n-1) -> (0, 0) can be treated as two men go from (0, 0) -> (n-1, n-1) together, 
but when they go into the same cell, they can pick up one cherry.
Using DP to solve the problem:
1.  dp[x1][y1][x2] to represent the largest ans we can get when first guy (marked as A) at(x1, y1) 
and second guy(marked as B) at (x2, x1 + y1 - x2), 只需要三个坐标是因为A和B是同时走的，走的步数是一样的。
2.  Induction: every time we calculate the maximum of :
    * dp[x1 - 1][y1][x2] : A down, B right
    * dp[x1][y1 - 1][x2] : A right, B right
    * dp[x1 - 1][y1][x2 - 1]: A down, B down
    * dp[x1][y1 - 1][x2 - 1]: A right, B down
    if the Max of these values is negative, then we don't have a path to this point
    else we have: dp[x1][y1][x2] = Max + grid[x1][y1] + grid[x2][y2] (if A, B不在同一点 else only pick up one cherry)
3.  Base case;
    we use dp[][][]from 1 - n, so we have:
        dp[1][1][1] = 1 and all other values are MIN_VALUE
4.  Time: O(n^3); Space: O(n^3)
"""
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[float("-inf") for _ in range(n)] for _ in range(n)] for _ in range(n)]
        dp[0][0][0] = grid[0][0]
        for x1 in range(n):
            for y1 in range(n):
                for x2 in range(n):
                    y2 = x1 + y1 - x2
                    if y2 < 0 or y2 >= n:       # if out of bound
                        continue
                    if grid[x1][y1] == -1 or grid[x2][y2] == -1:    # if meets thorn
                        continue
                    if dp[x1][y1][x2] > 0:      # if already visited
                        continue

                    curr_max = max(dp[x1 - 1][y1][x2], dp[x1 - 1][y1][x2 - 1], dp[x1][y1 - 1][x2], dp[x1][y1 - 1][x2 - 1])
                    if curr_max < 0:        # cannot get to this location
                        continue
                        
                    dp[x1][y1][x2] = curr_max + grid[x1][y1]   # person A pick up the cherry
                    if not (x1 == x2 and y1 == y2):
                        dp[x1][y1][x2] += grid[x2][y2]         # person B pick up the cherry if A, B不在同一点
        
        return 0 if dp[-1][-1][-1] == float("-inf") else dp[-1][-1][-1]



"""
solution 2: dfs + memo, top down DP https://leetcode.com/problems/cherry-pickup/discuss/109907/Simple-Python-DP-solution-n3-timespace
"""
