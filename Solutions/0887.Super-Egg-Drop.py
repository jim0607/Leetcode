"""
887. Super Egg Drop

You are given K eggs, and you have access to a building with N floors from 1 to N. 

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.

Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 

Your goal is to know with certainty what the value of F is.

What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?


Example 1:

Input: K = 1, N = 2
Output: 2
Explanation: 
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.
Example 2:

Input: K = 2, N = 6
Output: 3
Example 3:

Input: K = 3, N = 14
Output: 4
"""



"""
这道题说给了我们K个鸡蛋，还有一栋共N层的大楼，说是鸡蛋有个临界点的层数F，高于这个层数扔鸡蛋就会碎，否则就不会，
问我们找到这个临界点最小需要多少操作，注意这里的操作只有当前还有没碎的鸡蛋才能进行。
这道题是基于经典的扔鸡蛋的问题改编的，原题是有 100 层楼，为了测鸡蛋会碎的临街点，最少可以扔几次？
答案是只用扔 14 次就可以测出来了，讲解可以参见[油管上的这个视频](https://www.youtube.com/watch?v=NGtt7GJ1uiM)，
这两道题看着很相似，其实是有不同的。这道题限制了鸡蛋的个数K.
鸡蛋数K和楼层数N，所以就要使用一个二维数组 DP，其中 dp[i][j] 表示有i个鸡蛋，j层楼要测需要的最小操作数。
那么我们在任意k层扔鸡蛋的时候就有两种情况（注意这里的k跟鸡蛋总数K没有任何关系，k的范围是 [1, j]）：
鸡蛋碎掉：接下来就要用 i-1 个鸡蛋来测 k-1 层，所以需要 dp[i-1][k-1] 次操作。
鸡蛋没碎：接下来还可以用i个鸡蛋来测 j-k 层，所以需要 dp[i][j-k] 次操作。
因为我们每次都要面对最坏的情况，所以在第j层扔，需要 max(dp[i-1][k-1], dp[i][j-k])+1 步，状态转移方程为：
dp[i][j] = min(dp[i][j], 1 + max(dp[i - 1][k - 1], dp[i][j - k])) ( 1 <= k < j )
"""
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
        for j in range(N+1):
            dp[1][j] = j
        for i in range(2, K+1):
            for j in range(1, N+1):
                dp[i][j] = j
                for k in range(1, j):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][k-1], dp[i][j-k]))
        return dp[-1][-1]
"""
Time - O(KN^2) - TLE
"""

"""
In the above solution, we use for k in range(1, j) loop to find a k, so that max(dp[i-1][k-1], dp[i][j-k]) is minimized.
若我们仔细观察 dp[i - 1][k - 1] 和 dp[i][j - k]，可以发现前者是随着k递增，后者是随着k递减，且每次变化的值最多为1，
所以只要存在某个k值使得二者相等，那么就能得到最优解，否则取最相近的两个k值做比较，
由于这种单调性，我们其实可以不需要for k in range(1, j) loop做线性查找，我们可以在 [1, j] 范围内对k进行二分查找，
找到第一个使得 dp[i - 1][k - 1] 不小于 dp[i][j - k] 的k值，然后用这个k值去更新 dp[i][j] 即可，这样时间复杂度就减少到了 O(KNlogN).
"""
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
        for j in range(N+1):
            dp[1][j] = j
        for i in range(2, K+1):
            for j in range(1, N+1):
                dp[i][j] = j
                k = self._binary_search(dp, i, j)
                dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][k-1], dp[i][j-k]))
        return dp[-1][-1]
    
    def _binary_search(self, dp, i, j):     # binary search to find the first k to satisfy dp[i-1][k-1] >= dp[i][j-k]
        start, end = 1, j - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if dp[i-1][mid-1] >= dp[i][j-mid]:
                end = mid
            else:
                start = mid
        return start if dp[i-1][start-1] >= dp[i][j-start] else end
