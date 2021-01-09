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

    
    
"""
优化为O(N^2), 用一个isPalin[i][j]记录s[i:j]是否是palindrome, 更新isPalin[i][j]的方法与leetcode 5 相同，
这样就不用每次都用双指针去判断s[i:j]是不是palindrome
"""
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
    
    
    
"""
backtrack结束条件: curr_idx = len(s) - 1
constraints on next_candidates: s[curr_idx+1:next_idx+1] has to be panlind
arguments pass into backtrack function: curr_idx, curr_cnt

naive backtrack takes O(N*2^N)
"""
class Solution:
    def minCut(self, s: str) -> int:
        def backtrack(curr_idx, curr_cnt):
            if curr_idx == len(s) - 1:
                self.min_cnt = min(self.min_cnt, curr_cnt)
                return
            
            for next_idx in range(curr_idx + 1, len(s)):
                next_substr = s[curr_idx + 1: next_idx + 1]
                if is_palin(next_substr):
                    backtrack(next_idx, curr_cnt + 1)
                    
        
        def is_palin(t):
            i, j = 0, len(t) - 1
            while i < j:
                if t[i] != t[j]:
                    return False
                i += 1
                j -= 1
            return True
                
        
        self.min_cnt = len(s)
        backtrack(-1, 0)
        return self.min_cnt - 1
    
    
"""
backtrack with memorization takes O(N^3)
"""
class Solution:
    def minCut(self, s: str) -> int:
        def backtrack(curr_idx):
            if curr_idx == len(s) - 1:
                return 0 
            
            if curr_idx in memo:
                return memo[curr_idx]
            
            min_cnt = sys.maxsize
            for next_idx in range(curr_idx + 1, len(s)):  # for each curr_idx, there are at most N choices for next_idx, so O(N^2)
                next_substr = s[curr_idx + 1: next_idx + 1]
                if is_palin(next_substr):
                    min_cnt = min(min_cnt, 1 + backtrack(next_idx))
            
            memo[curr_idx] = min_cnt
            return min_cnt
                    
        
        def is_palin(t):    # O(N)
            i, j = 0, len(t) - 1
            while i < j:
                if t[i] != t[j]:
                    return False
                i += 1
                j -= 1
            return True
                
        
        memo = defaultdict(int)     # curr_idx --> from curr_idx, what is the minimum cnt
        return backtrack(-1) - 1    # return from curr_idx, what is the minimum cnt

    
    
"""
precalculation + backtrack with memorization takes O(N^2)
"""
class Solution:
    def minCut(self, s: str) -> int:
        def backtrack(curr_idx):
            if curr_idx == len(s) - 1:
                return 0 
            
            if curr_idx in memo:
                return memo[curr_idx]
            
            min_cnt = sys.maxsize
            for next_idx in range(curr_idx + 1, len(s)):  # for each curr_idx, there are at most N choices for next_idx, so O(N^2)
                next_substr = s[curr_idx + 1: next_idx + 1]
                if dp[curr_idx + 1][next_idx]:
                    min_cnt = min(min_cnt, 1 + backtrack(next_idx))
            
            memo[curr_idx] = min_cnt
            return min_cnt
                    
        
        dp = self.pre_calculate_palin(s)    # pre-calculate dp[i][j] = is s[i:j] a palin?

        memo = defaultdict(int)     # curr_idx --> from curr_idx, what is the minimum cnt
        return backtrack(-1) - 1    # return from curr_idx, what is the minimum cnt
    
    
    def pre_calculate_palin(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]  # dp[i][j] = is s[i:j] a palin?
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = True if i + 1 == j else dp[i+1][j-1]
                    
        return dp
