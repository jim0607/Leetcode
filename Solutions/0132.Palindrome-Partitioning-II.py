"""
132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""



"""
f[j]=the minimum number of total palindrom a palindrome partitining till the jth character (not including j meaning the last palindrome should end with the j-1th character)
f[j]=min(f[i]+1) for i<j and s[i:j] is palindrome
O(N^3)
"""
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [n for _ in range(n + 1)]
        dp[0] = -1
        dp[1] = 0
        for j in range(2, n+1):
            for i in range(j):
                if self._is_panlin(s[i:j]):
                    dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]
    
    def _is_panlin(self, t):
        left, right = 0, len(t) - 1
        while left < right:
            if t[left] != t[right]:
                return False
            left += 1
            right -= 1
        return True

    
    
""""
优化为O(N^2), 用一个isPalin[i][j]记录s[i:j]是否是palindrome, 更新isPalin[i][j]的方法与leetcode 5 相同，
这样就不用每次都用双指针去判断s[i:j]是不是palindrome
""
class Solution:
    def minCut(self, s: str) -> int:
        
        # step 1: pre-calculate the palindeome and store them in matrix - same as 5. Longest Palindromic Substring
        n = len(s)
        palin = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            palin[i][i] = True
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j == i + 1:
                        palin[i][j] = True
                    else:
                        palin[i][j] = palin[i+1][j-1]    
                        
        # step 2: dp to update minimum cuts
        dp = [n for _ in range(n + 1)]  # dp[i]=the min cuts needed to partition to ith, not including i
        dp[0] = -1
        dp[1] = 0
        for j in range(2, n+1):
            for i in range(j):
                if palin[i][j-1]:
                    dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]
