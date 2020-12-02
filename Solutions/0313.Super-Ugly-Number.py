"""
313. Super Ugly Number

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
"""


"""
heap solution: O(nlog(kn)) where k is the lens of primes list
"""
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        added = set()
        added.add(1)
        hq = [1]
        for _ in range(n):
            curr_min = heappop(hq)
            for prime in primes:
                if prime * curr_min not in added:
                    heappush(hq, prime * curr_min)
                    added.add(prime * curr_min)
        return curr_min
