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
