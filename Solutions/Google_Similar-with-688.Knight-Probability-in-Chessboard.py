"""
Given a game board, a coordinate, and a number n,
find the number of ways you can travel up, down, left, right n steps and still end up at the original coordinate.
n = 0: 1
n = 1: 0
n = 2: 4
n = 3: 0
n = 4: (1 + 4 + 4)*4 = 36 可以画出来，第一步选择往上走的话有9中可能回到原点，所以又4*9=36种可能
"""

"""
解法：similar with 688. Knight Probability in Chessboard
dp[i][j][k] = from (i, j) the number of ways you to end up at the original coordinate with k steps
dp[i][j][k] = dp[i - 1][j][k - 1] + dp[i][j - 1][k - 1] + dp[i + 1][j][k - 1] + dp[i][j + 1][k - 1]
dp[0][0][0] = 1
"""

def ways_to_travel(m, n, K, r, c):
    """
    :param m, n: dimension of the board
    :param K: the total steps
    :param r: row of the original coordinate
    :param c: col of the original coordinate
    :return: the number of ways to travel K steps from (r, c), and finally get back to (r, c)
    """
    dp = [[[0 for _ in range(K + 1)] for _ in range(n)] for _ in range(m)]  # 注意 K + 1
    dp[r][c][0] = 1     # note that dp[other_than_r][other_than_c][0] = 0
    for k in range(1, K + 1):   # 特别注意三个for 循环K是在最外面的
        for i in range(m):
            for j in range(n):
                for delta_i, delta_j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    neigh_i, neigh_j = i + delta_i, j + delta_j
                    if 0 <= neigh_i < m and 0 <= neigh_j < n:
                        dp[i][j][k] += dp[neigh_i][neigh_j][k-1]   # 代表 prev_i, prev_j 
    return dp[r][c][K]

print(ways_to_travel(10, 10, 4, 2, 2))
