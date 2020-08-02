650. 2 Keys Keyboard

Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
 

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.


"""
其实是一个质因数分解的问题(integer factorization);
dp[j] = min steps to get j
"""
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        dp[1] = 0
        for j in range(2, n + 1):
            for i in range(j - 1, 0, -1):
                if j % i == 0:
                    dp[j] = dp[i] + j // i
                    break       # i 倒着遍历，碰到第一个能整除的就可以break了
        return dp[n]
