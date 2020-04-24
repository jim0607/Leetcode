516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".



"""dp[i][j]=dp[i+1][j-1]+2 if s[i]==s[j] else max(dp[i+1][j], dp[i][j-1])
注意初始化对角线，因为计算dp[i]需要用到dp[i+1]，所以要先算i+1, 再算i"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        lens = len(s)
        if lens <= 1:
            return lens
        
        dp = [[1] * lens for _ in range(lens)]     # longest palindr subsequence from i to j, including i and j
        for i in range(lens):
            dp[i][i] = 1
            if i + 1 < lens:
                dp[i][i + 1] = 2 if s[i] == s[i + 1] else 1
                
        for j in range(1, lens):
            for i in range(j - 2, -1, -1):      ## 注意 i 要倒序遍历
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    
        return dp[0][lens - 1]

    
"""解法一：递归, O(?)"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def _helper_(s):
            if len(s) <= 1:
                return len(s)
            if s[0] == s[-1]:
                return _helper_(s[1:-1]) + 2
            else:
                return max(_helper_(s[1:]), _helper_(s[:-1]))
        return _helper_(s)
        
        
        
"""解法二：下面是带memo的递归形式的解法，memo数组这里起到了一个缓存已经计算过了的结果，这样能提高运算效率，使其不会time limit ecceeded TLE
O(N^2), O(N^2)"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        lens = len(s)
        memo = [[-1]*lens for _ in range(lens)]
        return self._helper_(s, 0, lens-1, memo)
        
    def _helper_(self, s, left, right, memo):
        if left > right:
            return 0
        if left == right:
            return 1
        if memo[left][right] != -1:
            return memo[left][right]   # 只要memo[left][right]被计算过，就直接调用memo[left][right]，就不用再计算一遍了
        if s[left] == s[right]:
            memo[left][right] = self._helper_(s, left+1, right-1, memo) + 2
        else:
            memo[left][right] = max(self._helper_(s, left+1, right, memo), self._helper_(s, left, right-1, memo))
            
        return memo[left][right]
        
        
"""解法三：参考递归法的思路尝试一下DP； O(N^2), O(N^2)
动态规划四要素：
1. dp[i][j]表示字符串s[i:j]的最长回文子序列的长度
2. 递推关系：dp[i][j] = dp[i+1][j-1]+2 当s[i]=s[j]
dp[i][j]=max(dp[i+1][j],dp[i][j-1]) 当s[i]!=s[j] 取s[i+1..j] 和s[i..j-1]中最长的 由于dp[i][j]需要dp[i+1][j]所以需要i逆序枚举s的长度，而又因为dp[i][j]需要dp[i][j-1],所以要求j是递增的，这样在保证求解dp[i][j]时,dp[i][j-1]肯定已经求解过了，又由于dp[i][j]表示从i到j的字符串的最长回文子序列的长度，所以要保证j大于i，所以j从i+1开始遍历。这样就可以保证这样可以保证每个子问题都已经算好了。
3. 初始化dp[i][i] = 1 单个字符的最长回文序列是 1
4. 结果：dp[0][lens-1]"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        lens = len(s)
        dp = [[0]*lens for _ in range(lens)]
        for i in range(lens):
            dp[i][i] = 1
        for i in range(lens-1, -1, -1):
            for j in range(i+1, lens):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][lens-1]
        
        
        
        
"""解法四：优化成一位数组 DP； O(N^2), O(N)
然后在遍历过程中，你会发现，你只需要j位置的数据，不需要之前的，所以可以把二维变成两个一维数组。要好好体会理解"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        lens = len(s)
        if lens <= 1:
            return lens
        dp = [1]*lens
        for i in range(lens-1, -1, -1):
            prev = 0
            for j in range(i+1, lens):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = prev + 2
                prev = max(temp, prev)
        return max(dp)
