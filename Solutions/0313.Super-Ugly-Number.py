313. Super Ugly Number

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.


"""
heap solution: O(nlog(kn)) where k is the lens of primes list
"""

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        hq = [1]
        included = set()
        included.add(1)
        
        for _ in range(n - 1):
            currmin = heappop(hq)
            for prime in primes:
                nextnum = currmin * prime
                if nextnum not in included:
                    heappush(hq, nextnum)
                    included.add(nextnum)
                    
        return heappop(hq)
