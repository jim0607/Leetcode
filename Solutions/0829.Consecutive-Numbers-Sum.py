"""
829. Consecutive Numbers Sum

Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
"""


"""
假设从x开始存在连续有k个加起来等于N, then x+(x+1)+...+(x+k-1) = N, ie: kx + k(k-1)/2 = N.
kx = N - k(k-1)/2. x = (N - k(k-1)/2) / k.  so the problem becomes: for k in range(1, N),
is there a number k, such that (N - k(k-1)/2) / k is an integer?
"""
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        k = 1
        cnt = 0
        while N - k * (k - 1) / 2 > 0:
            if (N - k * (k - 1) / 2) % k == 0:
                cnt += 1
            k += 1
            
        return cnt
