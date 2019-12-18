A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times. 

Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be obtained with exact n rolls.

Two sequences are considered different if at least one element differs from each other. Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 2, rollMax = [1,1,2,2,2,3]
Output: 34
Explanation: There will be 2 rolls of die, if there are no constraints on the die, there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.


"""没时间看明白，先贴上完成今天的任务吧"""
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        Max, mod = max(rollMax), 10**9 + 7
        dp = [[[0]*Max for _ in range(6)] for _ in range(n)] 
        for i in range(6): 
            dp[0][i][0] = 1
        for i in range(1, n):
            for j in range(6):
                dp[i][j][0] = sum(dp[i-1][t][k] for t in range(6) for k in range(rollMax[t]) if t != j)%mod
                for k in range(rollMax[j]-1, 0, -1):
                    dp[i][j][k] = dp[i-1][j][k-1]
        return sum(dp[n-1][j][k] for j in range(6) for k in range(Max)) % mod
