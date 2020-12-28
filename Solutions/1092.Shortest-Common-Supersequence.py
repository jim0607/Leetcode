"""
1092. Shortest Common Supersequence

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  
If multiple answers exist, you may return any of them.

(A string S is a subsequence of string T if deleting some number of characters from T 
(possibly 0, and the characters are chosen anywhere from T) results in the string S.)

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
"""


"""
solution 1: naive backtrack - O(2^(M+N))
backtrack结束条件: curr_idx1 == len(s1) - 1 and curr_idx2 == len(s2) - 1
constraint for next_candidate: we can choose s1[next_idx1] as the next_ch or s2[next_idx2]
arguments pass into backtrack function: curr_idx1, curr_idx2, curr_comb
"""
class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        def backtrack(curr_idx1, curr_idx2, curr_comb):
            if curr_idx1 == m - 1 and curr_idx2 == n - 1:
                if len(curr_comb) < self.min_len:
                    self.min_len = len(curr_comb)
                    self.res = curr_comb
                return
            
            if curr_idx1 == m - 1:
                backtrack(curr_idx1, curr_idx2 + 1, curr_comb + s2[curr_idx2 + 1])
            elif curr_idx2 == n - 1:
                backtrack(curr_idx1 + 1, curr_idx2, curr_comb + s1[curr_idx1 + 1])
            else:
                if s1[curr_idx1 + 1] == s2[curr_idx2 + 1]:
                    backtrack(curr_idx1 + 1, curr_idx2 + 1, curr_comb + s1[curr_idx1 + 1])
                else:
                    backtrack(curr_idx1, curr_idx2 + 1, curr_comb + s2[curr_idx2 + 1])
                    backtrack(curr_idx1 + 1, curr_idx2, curr_comb + s1[curr_idx1 + 1])
            
            
            
        m, n = len(s1), len(s2)
        self.min_len = m + n
        self.res = s1 + s2
        backtrack(-1, -1, "")
        return self.res

        
"""
solution 2: recursion + memorization (bottom up dp) - O(MN)
"""
class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        def backtrack(curr_idx1, curr_idx2):
            if curr_idx1 == m - 1 and curr_idx2 == n - 1:
                return ""
            
            if (curr_idx1, curr_idx2) in memo:
                return memo[(curr_idx1, curr_idx2)]
            
            res = s1 + s2
            if curr_idx1 == m - 1:
                ans = s2[curr_idx2 + 1] + backtrack(curr_idx1, curr_idx2 + 1)
                if len(ans) < len(res):
                    res = ans
            elif curr_idx2 == n - 1:
                ans = s1[curr_idx1 + 1] + backtrack(curr_idx1 + 1, curr_idx2)
                if len(ans) < len(res):
                    res = ans
            else:
                if s1[curr_idx1 + 1] == s2[curr_idx2 + 1]:
                    ans = s1[curr_idx1 + 1] + backtrack(curr_idx1 + 1, curr_idx2 + 1)
                    if len(ans) < len(res):
                        res = ans
                else:
                    ans1 = s2[curr_idx2 + 1] + backtrack(curr_idx1, curr_idx2 + 1)
                    ans2 = s1[curr_idx1 + 1] + backtrack(curr_idx1 + 1, curr_idx2)
                    if len(ans1) < len(res):
                        res = ans1
                    if len(ans2) < len(res):
                        res = ans2
                        
            memo[(curr_idx1, curr_idx2)] = res
            return res
            

        m, n = len(s1), len(s2)
        memo = defaultdict(int)   # (curr_idx1, curr_idx2) --> start from (curr_idx1, curr_idx2), the SCS
        return backtrack(-1, -1)  # returns start from (-1, -1), the SCS
        
        
"""
solution 3: top down dp - O(MN)
step 1: construct_dp_table
step 2: get_result_by_reversely_traverse_dp_table
"""
class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        dp = self.construct_dp_table(s1, s2)
        res = self.get_result_by_reversely_traverse_dp_table(s1, s2, dp)
        return res
    
    def construct_dp_table(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [[m + n] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        return dp
        
    def get_result_by_reversely_traverse_dp_table(self, s1, s2, dp):
        m, n = len(s1), len(s2)
        res = ""
        i, j = m, n
        while i >= 1 and j >= 1:
            if s1[i-1] == s2[j-1]:
                res += s1[i-1]
                i -= 1
                j -= 1
            else:
                if dp[i][j] == 1 + dp[i-1][j]:
                    res += s1[i-1]
                    i -= 1
                elif dp[i][j] == 1 + dp[i][j-1]:
                    res += s2[j-1]
                    j -= 1
        while i >= 1:
            res += s1[i-1]
            i -= 1
        while j >= 1:
            res += s2[j-1]
            j -= 1
            
        return res[::-1]    
