Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.


"""f[i]=the least number of perfect square numbers which sum to i
f[j] = min(f[j-i^2]+1) for i^2<=j
Time complexity: j is from 0 to n, i is from 0 to j^0.5, so O(N^1.5)"""
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        for j in range(2, n + 1):
            i = 1
            while i**2 <= j:
                dp[j] = min(dp[j], dp[j - i**2] + 1)
                i += 1
                
        return dp[n]
    
    
    
"""
solution 2: level order BFS.
Given a N-ary tree, where each node represents a __remainder__ of the number n subtracting a combination of square numbers, 
our task is to find a node in the tree, which should meet the conditions or remainder=0.
Time complexity: 比较复杂最后是 O(n^(h/2)), where h is the height of the N-ary tree, h is 0 to 4
"""
class Solution(object):
    def numSquares(self, n):
        squares = [i*i for i in range(1, n+1) if i*i <= n]
        q = collections.deque()
        q.append(n)
        visited = set()
        visited.add(n)
        level = 0
        while q:
            level += 1
            lens = len(q)
            for _ in range(lens):
                curr_remain = q.popleft()
                for sq in squares:
                    next_remain = curr_remain - sq
                    if next_remain < 0:
                        continue
                    if next_remain == 0:
                        return level
                    if next_remain in visited:
                        continue
                    q.append(next_remain)
                    visited.add(next_remain)
                
        return level
