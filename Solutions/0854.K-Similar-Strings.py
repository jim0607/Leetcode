854. K-Similar Strings

Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly K times so that the resulting string equals B.

Given two anagrams A and B, return the smallest K for which A and B are K-similar.

Example 1:

Input: A = "ab", B = "ba"
Output: 1
Example 2:

Input: A = "abc", B = "bca"
Output: 2
Example 3:

Input: A = "abac", B = "baca"
Output: 2
Example 4:

Input: A = "aabc", B = "abca"
Output: 2



"""
求一个状态到另一个状态的最短路径: bfs, 想要速度更快？双端 + Prune!
solution 1: 双端
"""
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        q_A, q_B = collections.deque(), collections.deque()
        visited_A, visited_B = set(), set()
        q_A.append(A)
        q_B.append(B)
        visited_A.add(A)
        visited_B.add(B)
        
        step = 0
        while q_A and q_B:
            if visited_A & visited_B:
                return step
            self._bfs(q_A, visited_A)   # 双端bfs的目的只是更新q和visited
            step += 1
            if visited_A & visited_B:
                return step
            self._bfs(q_B, visited_B)
            step += 1
        
    def _bfs(self, q, visited):         # 双端bfs中，每次bfs只走一层
        for _ in range(len(q)):
            curr = q.popleft()
            for next in self._swap(curr):   # takes O(N^2)
                if next in visited:
                    continue
                q.append(next)
                visited.add(next)
                
    def _swap(self, s):         # takes O(N^2)
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                yield s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                
                
                
                
"""
solution 2: prune: How to prune?  there are so many swaps, how to make sure we choose swaps that are leading next_node cloaser to B?
1. while S[i]==B[i], we don't need to swap them, until we found S[i]!=B[i], then ith pos needs to be swapped; 
2. swapped with whom? we find S[j]==B[i], then swap j and i in S, now B[i]==S[i], and S is getting closer to B!
"""
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        q = collections.deque()
        visited = set()
        q.append(A)
        visited.add(A)
        
        step = -1
        while q:
            step += 1
            lens = len(q)
            for _ in range(lens):
                curr = q.popleft()
                if curr == B:
                    return step
                for next in self._swap(curr, B):   # takes O(N)
                    if next in visited:
                        continue
                    q.append(next)
                    visited.add(next)
                
    def _swap(self, s, B):    # now only takes O(N)
        i = 0
        while s[i] == B[i]:   # if S[i]==B[i], we don't need to swap them - strong prune to makes sure swapped string always get more and more similar with B
            i += 1
        for j in range(i + 1, len(s)):
            if s[j] == B[i]:  # since B[i]!=s[i], if we swap s[j] to s[i], now B[i]=s[i]: this is how every swap make sure we get more and more closer to B
                yield s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
