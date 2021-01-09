#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (43.92%)
# Likes:    1317
# Dislikes: 51
# Total Accepted:    195.4K
# Total Submissions: 443.2K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#


"""
要求输出所有的可能组合，所以只能backtrack. O(L*2^L), where L is the lens of string, 2 is two choices: 这这里分还是不分。  
如果题目只是要求输出所有可能组合的数目，那就dp - O(L^2)
end condition: curr_idx == len(s) - 1
constraint on next candidate: next_s should be palin
parameters pass into backtrack: (curr_idx, curr_comb)
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(curr_idx, curr_comb):
            if curr_idx == len(s) - 1:
                res.append(curr_comb.copy())
                return
            for next_idx in range(curr_idx + 1, len(s)):
                next_s = s[curr_idx + 1: next_idx + 1]
                if is_palind(next_s):
                    curr_comb.append(next_s)
                    backtrack(next_idx, curr_comb)
                    curr_comb.pop()
                    
                    
        def is_palind(t):       # O(L)
            i, j = 0, len(t) - 1
            while i < j:
                if t[i] != t[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        
        res = []
        backtrack(-1, [])
        return res

"""
可以像132. Palindrome Partitioning II 那样先把is_palin[i][j]提前算好，这样就不需要用O(L)去判断is_palind(next_s)了
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(curr_idx, curr_comb):
            if curr_idx == len(s) - 1:
                res.append(curr_comb.copy())
                return
            
            for next_idx in range(curr_idx + 1, len(s)):
                next_sub = s[curr_idx + 1 : next_idx + 1]
                if dp[curr_idx + 1][next_idx]:
                    curr_comb.append(next_sub)
                    backtrack(next_idx, curr_comb)
                    curr_comb.pop()
        
        
        dp = self.get_palin(s)      # 把is_palin[i][j]提前算好
        res = []
        backtrack(-1, [])
        return res
        
    
    def get_palin(self, s):
        # dp[i][j] = is s[i:j] including i and j, is palin?
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = True if i + 1 == j else dp[i+1][j-1]
        return dp
    


"""
这种输出所有组合问题无脑使用dfs，想想如何套用Subsets的模板，然后再开始写
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.dfs(s, 0, [])
        return self.res
    
    def dfs(self, s, startIdx, curr):
        """递归的定义：从s中的start位置开始，挑一些位置切割，判断从start到i的部分是否为回文，
        如果是就放入curr中，如果i到了string末尾了则说明此事curr是一种组合方式，放入res中"""
        if startIdx == len(s):
            self.res.append(curr.copy())
            return
        
        for i in range(startIdx, len(s)):
            if not self.isPalin(s[startIdx:i + 1]):
                continue
                
            curr.append(s[startIdx:i + 1])
            self.dfs(s, i + 1, curr)
            curr.pop()
           
    def isPalin(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        
        return True
