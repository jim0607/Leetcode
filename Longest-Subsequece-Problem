一般来说，这类问题都是让你求一个最长子序列，因为最短子序列就是一个字符嘛，没啥可问的。一旦涉及到子序列和最值，那几乎可以肯定，考察的是动态规划技巧，时间复杂度一般都是 O(n^2)。
模板1：
lens = len(S)
dp = [[]*lens for _ in range(lens)]

for left in range(lens-1, -1, -1):
    for right in range(i+1, lens):
        if -----:
            dp[left][right] = 最值(dp[left+1][right-1].......)

模板2：
lens = len(S)
dp = [0]*lens

for i in range(lens-1, -1, -1):
    for j in range(i+1, lens):
        if -----:
            dp[j] = 最值(dp[j], dp[j-1]+...)
