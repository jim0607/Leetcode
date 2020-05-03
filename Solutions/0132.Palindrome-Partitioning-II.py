132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.


"""f[j]=the minimum number of total palindrom a palindrome partitining till the jth character (not including j meaning the last palindrome should end with the j-1th character)
f[j]=min(f[i]+1) for i<j and s[i:j] is palindrome
O(N^3)
"""
class Solution:
    def minCut(self, s: str) -> int:
        if not s:
            return 0
        
        lens = len(s)
        dp = [float("inf")] * (lens + 1)
        dp[0] = 0
        
        for j in range(1, lens + 1):
            for i in range(j):
                if self.isPalindrome(s[i:j]):   # the last palindrome should include jth character
                    dp[j] = min(dp[i] + 1, dp[j])

        return dp[-1] - 1       # 注意题目问的是最少划分几次
    
    def isPalindrome(self, s):
        if len(s) <= 1:
            return True
        
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
            
        return True

    
""""
优化为O(N^2), 用一个isPalin[i][j]记录s[i:j]是否是palindrome, 更新isPalin[i][j]的方法与leetcode 5 相同，
这样就不用每次都用双指针去判断s[i:j]是不是palindrome
""
class Solution:
    def minCut(self, s: str) -> int:
        lens = len(s)
        if lens == 0:
            return 0
        if lens == 1:
            return 0
        
        # dp[i]=the min cuts needed to partition to ith, not including i
        dp = [float("inf") for _ in range(lens + 1)]   
        dp[0] = 0
        
        # # isPalin[i][j]=if it is a palin from i->j, not including j, basically s[i:j]
        isPalin = [[False for _ in range(lens + 1)] for _ in range(lens + 1)]
        
        for j in range(1, lens + 1):
            for i in range(j):
                if s[i] == s[j - 1]:
                    if j - 1 - i <= 1:      # 初始化isPalin
                        isPalin[i][j] = True
                    else:
                        isPalin[i][j] = isPalin[i + 1][j - 1]
                        
                if isPalin[i][j]:
                    dp[j] = min(dp[j], dp[i] + 1)
                    
        return dp[lens] - 1
