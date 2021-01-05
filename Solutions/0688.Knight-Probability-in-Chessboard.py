"""
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. 
The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. 
Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
"""

"""
上论坛看大家的解法，结果发现都是换了一个角度来解决问题的，并不很关心骑士的起始位置，
而是把棋盘上所有位置上经过K步还留在棋盘上的走法总和都算出来，那么最后直接返回需要的值即可。
跟之前那道Out of Boundary Paths没啥本质上的区别，又是换了一个马甲就不会了系列。还是要用DP来做，
我们可以用三维DP数组，也可以用二维DP数组来做，这里为了省空间，我们就用二维DP数组来做，
其中dp[i][j]表示在棋盘(i, j)位置上走完当前步数还留在棋盘上的走法总和(注意是走法，不是步数)，初始化为1，
我们其实将步骤这个维度当成了时间维度在不停更新。好，下面我们先写出8种‘日’字走法的位置的坐标，
就像之前遍历迷宫上下左右四个方向坐标一样，这不过这次位置变了而已。
然后我们一步一步来遍历，每一步都需要完整遍历一遍棋盘的每个位置，新建一个临时数组t，大小和dp数组相同，但是初始化为0，
然后对于遍历到的棋盘上的每一个格子，我们都遍历8中解法，如果新的位置不在棋盘上了，
直接跳过，否则就加上上一步中的dp数组中对应的值，遍历完棋盘后，将dp数组更新为这个临时数组t
"""

"""
其中dp[i][j][k]表示在棋盘(i, j)位置上走完k步数还留在棋盘上的走法总和(注意是走法，不是步数)
dp[i][j][k] = from (i, j), we move k steps, how many ways to stay on the board.
move k steps, how many ways are there 8 ** k.
"""
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        steps = [[1,2], [1,-2], [-1,2], [-1,-2], [2,1], [2,-1], [-2,1], [-2,-1]]
        
        dp = [[[0 for _ in range(K + 1)] for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                dp[i][j][0] = 1
                
        for k in range(1, K + 1):     # 千万注意是先更新k, 不然后面的转移方程就不成立了
            for i in range(N):
                for j in range(N):
                    for delta_i, delta_j in steps:
                        neigb_i, neigb_j = i + delta_i, j + delta_j
                        if 0 <= neigb_i < N and 0 <= neigb_j < N:
                            dp[i][j][k] += dp[neigb_i][neigb_j][k-1]      # 表示从(prev_i, prev_j)跳到(i, j)
                            
        return dp[r][c][K] / 8**K




class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1
        dp = [[1]*N for _ in range(N)]
        steps = [[1,2], [1,-2], [-1,2], [-1,-2], [2,1], [2,-1], [-2,1], [-2,-1]]
        
        # 走K次，就做K张路径表，每次路径表cur只跟前一次的路径表pre有关
        for k in range(K):
            temp = [[0]*N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for step in steps:
                        x, y = i+step[0], j+step[1]
                        if 0 <= x < N and 0 <= y < N:
                            temp[x][y] += dp[i][j]   # temp[i][j] += dp[x][y]也可以，只是没那么好理解！
            dp = temp
        return dp[r][c]/(8**K)
