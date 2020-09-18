"""
651. 4 Keys Keyboard

Imagine you have a special keyboard with the following keys:

Key 1: (A): Print one 'A' on screen.

Key 2: (Ctrl-A): Select the whole screen.

Key 3: (Ctrl-C): Copy selection to buffer.

Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.

Example 1:
Input: N = 3
Output: 3
Explanation: 
We can at most get 3 A's on screen by pressing following key sequence:
A, A, A
Example 2:
Input: N = 7
Output: 9
Explanation: 
We can at most get 9 A's on screen by pressing following key sequence:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
"""



"""
dp[j] = max number pressing j times.
dp[j] = max(dp[i] * (j-i-1)), eg: i = j - 3; dp[j] = dp[j-3]*2, 因为把dp[j-3] ctr+V了一次; 
eg: i = j - 4, dp[j] = dp[j-4]*3, 因为把dp[j-4] ctr+V了两次
"""
class Solution:
    def maxA(self, N: int) -> int:
        if N == 1:
            return 1
        
        dp = [0 for _ in range(N + 1)]
        dp[1] = 1
        dp[2] = 2
        for j in range(3, N + 1):
            dp[j] = dp[j-1] + 1      # 注意初始化
            for i in range(1, j-2):     # 可以ctrl+v的次数是 j-2-i
                dp[j] = max(dp[j], dp[i] * (j-i-1))
            
        return dp[N]
