"""
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.
"""


"""
f[i][j]=当石子还剩i到j时，先手最多能赢多少
f[i][j] = max(取左边A[i]-f[i+1][j], 取右边A[j]-f[i][j-1])
"""
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2: return True
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if j == i + 1:
                    dp[i][j] = abs(nums[j] - nums[i])
                else:
                    dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
                    
        return dp[0][n-1] >= 0


    
    
    
    
"""时间复杂度：O(2^N)，其中 N 是数组的长度。空间复杂度：O(N)，为递归时栈使用的空间。"""
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        sumNums = sum(nums)
        firstMax = self._getMax(nums, 0, len(nums)-1)
        return firstMax >= sumNums-firstMax

    def _getMax(self, nums, i, j) -> int:
        if i == j:   # if there are odd number os elements
            return nums[i]
        elif i+1 == j:
            return max(nums[i], nums[j])
        
        # 都是聪明人，A如果想要赢A就取能保障自己赢的那个数让自己收益更大，这就是为什么大括号用max，A取完之后B来取，B也想要赢，于是B取剩下的数组中的能保证自己赢的那个数，于是B在剩余数组中取走属于自己的那份max，这样留给A下次来取的就是min了，这就是为什么小括号里用min
        return max(
            nums[i] + min(self._getMax(nums, i+1, j-1), self._getMax(nums, i+2, j)), 
            nums[j] + min(self._getMax(nums, i+1, j-1), self._getMax(nums, i, j-2))    )
