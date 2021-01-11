"""
397. Integer Replacement

Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.

Example 1:

Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1
Example 2:

Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1
Example 3:

Input: n = 4
Output: 2
"""


"""
similar with 991. Broken Calculator 
backtrack with memo - O(n)
"""
class Solution:
    def integerReplacement(self, n: int) -> int:
        def backtrack(n):
            if n == 1:
                return 0
            
            if n in memo:
                return memo[n]
            
            res = sys.maxsize
            if n % 2 == 1:
                res = 1 + min(backtrack(n + 1), backtrack(n - 1))
                memo[n] = res
                return res
            else:
                res = 1 + backtrack(n // 2)
                memo[n] = res
                return res     
        
        
        memo = defaultdict(int)
        return backtrack(n)
