1267. Count Servers that Communicate

You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
Example 2:

Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
Example 3:

Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.



"""
one pass to store the number of servers in each row and each col, cnt += 1.
another pass to find the isolated severs, cnt -= 1.
"""
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_cnt = collections.defaultdict(int)
        col_cnt = collections.defaultdict(int)
        
        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_cnt[i] += 1
                    col_cnt[j] += 1
                    cnt += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_cnt[i] == 1 and col_cnt[j] == 1):   # isolated sever
                        cnt -= 1
                        
        return cnt
