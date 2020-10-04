"""
552. Student Attendance Record II

Given a positive integer n, return the number of all possible attendance records with length n, 
which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8 
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 
"""


"""
typical backtrack - O(3^N)
"""
class Solution:
    def checkRecord(self, n: int) -> int:
        def backtrack(curr_comb, cnt_of_A):
            if len(curr_comb) == n:
                self.cnt += 1
                return
            
            for next_ch in ["A", "L", "P"]:
                if next_ch == "A":
                    if cnt_of_A == 1:
                        continue
                    curr_comb.append("A")
                    backtrack(curr_comb, cnt_of_A + 1)
                    curr_comb.pop()
                elif next_ch == "L":
                    if len(curr_comb) >= 2 and curr_comb[-1] == curr_comb[-2] == "L":
                        continue
                    curr_comb.append("L")
                    backtrack(curr_comb, cnt_of_A)
                    curr_comb.pop()
                elif next_ch == "P":
                    curr_comb.append("P")
                    backtrack(curr_comb, cnt_of_A)
                    curr_comb.pop()
        
        
        self.cnt = 0
        backtrack([], 0)        
        return self.cnt % (10**9 + 7)
        
        
        
"""
solution 2: dp - O(n). dp[i] = how many ways for i.
dp[1] = 3
dp[2] = 8
dp[3] = 19
If we don't have "A" in the record, then we have below:
dp[i] = dp[i-1] if choose ith ch to be "P".
dp[i] = dp[i-2] if choose the last two ch to be "PL"
dp[i] = dp[i-3] if choose last three ch to be "PLL", note that cannot be "LLL".
so dp[i] = dp[i-1] + dp[i-2] + dp[i-3] for the case there is not "A" in the record.
Now we have the dp[i] for the case with out "A".
Since we can add "A" anywhere, so the res = sum(dp[i-1] * dp[n-i]).
"""
class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 3
        if n == 2: return 8
        
        MOD = 10**9 + 7
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 2   # there are 2 ways of records without "A" if n == 1
        dp[2] = 4   # "PP", "PL", "LP", "LL"
        for i in range(3, n + 1):
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD
        
        res = dp[n]     # now dp[n] = ways of records without "A" in the record
        res += sum(dp[i-1] * dp[n-i] % MOD for i in range(1, n+1)) % MOD
        return res % MOD
