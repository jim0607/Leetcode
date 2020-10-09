"""
1563. Stone Game V

There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), 
then Bob calculates the value of each row which is the sum of the values of all the stones in this row. 
Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. 
If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's is initially zero.

Return the maximum score that Alice can obtain.

Example 1:

Input: stoneValue = [6,2,3,4,5,5]
Output: 18
Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.
Example 2:

Input: stoneValue = [7,7,7,7,7,7,7]
Output: 28
Example 3:

Input: stoneValue = [4]
Output: 0
"""


"""
dp[i][j] = the number of scores Alice can get for [i, j].
dp[i][i] = for k in range(i, j) max(dp[i][k], dp[k+1][j]) + min(sums[i, k], sums[k+1, j]).
O(N^3)
"""
class Solution:
    def stoneGameV(self, stones: List[int]) -> int:
        n = len(stones)
        pre_sum = [0 for _ in range(n + 1)]     # step 1: construct pre_sum for fast interval sum look up
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + stones[i]
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            if i + 1 < n:
                dp[i][i+1] = min(stones[i], stones[i+1])
        
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                for k in range(i, j):
                    left = pre_sum[k+1] - pre_sum[i]
                    right = pre_sum[j+1] - pre_sum[k+1]
                    if left > right:
                        dp[i][j] = max(dp[i][j], right + dp[k+1][j])
                    elif left < right:
                        dp[i][j] = max(dp[i][j], left + dp[i][k])
                    else:
                        dp[i][j] = max(dp[i][j], left + max(dp[i][k], dp[k+1][j]))
                        
        return dp[0][n-1]
    
"""
If we can prove k is the best when we make left and right evenly splitted,
then we can use binary search to find k. then time is O(N^2logN).
we can do binary search cuz as left increase, right decrease.
"""
""" Below does not work, so I think maybe even split left and right is not the best for choosing k. """
class Solution:
    def stoneGameV(self, stones: List[int]) -> int:
        n = len(stones)
        pre_sum = [0 for _ in range(n + 1)]     # step 1: construct pre_sum for fast interval sum look up
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + stones[i]
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            if i + 1 < n:
                dp[i][i+1] = min(stones[i], stones[i+1])
        
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                k = self._binary_search(pre_sum, i, j)
                left = pre_sum[k+1] - pre_sum[i]
                right = pre_sum[j+1] - pre_sum[k+1]
                if left == right:
                    dp[i][j] = max(dp[i][j], left + max(dp[i][k], dp[k+1][j])) 
                else:
                    left_2 = pre_sum[k+2] - pre_sum[i]
                    right_2 = pre_sum[j+1] - pre_sum[k+2]
                    dp[i][j] = max(dp[i][j], left + dp[i][k], right_2 + dp[k+2][j])  
        return dp[0][n-1]
    
    def _binary_search(self, pre_sum, i, j):
        """
        return the last idx k for left_sum < right_sum
        """
        start, end = i, j - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            left = pre_sum[mid+1] - pre_sum[i]
            right = pre_sum[j+1] - pre_sum[mid+1]
            if left >= right:
                end = mid
            else:
                start = mid
        return end if pre_sum[end+1] - pre_sum[i] < pre_sum[j+1] - pre_sum[end+1] else start
