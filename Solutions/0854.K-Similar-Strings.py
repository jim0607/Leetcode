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
"""
class Solution:
    def kSimilarity(self, start: str, end: str) -> int:
        q = collections.deque()
        visited = set()
        q.append(start)
        visited.add(start)
        
        steps = -1
        while len(q) > 0:
            steps += 1
            lens = len(q)
            for _ in range(lens):
                curr_node = q.popleft()
                if curr_node == end:
                    return steps
                for next_node in self._get_next(curr_node, end):
                    if next_node not in visited:
                        q.append(next_node)
                        visited.add(next_node)
    
    def _get_next(self, curr, end):     # takes O(N)
        i = 0
        # 寻找第一个不相同的ch的位置
        # if S[i]==B[i], we don't need to swap them - strong prune to makes sure swapped string always get more and more similar with B
        while i < len(curr) and curr[i] == end[i]:    
            i += 1
        for j in range(i+1, len(curr)):     # 找到第一个不相同的ch后, 我们需要在curr后面找等于那个ch的位置进行交换，这样就把curr[i]那个位置的ch换成与end[i]一样了，这样就离end又更近了一步
            if curr[j] == end[i]:
                yield curr[:i] + curr[j] + curr[i+1:j] + curr[i] + curr[j+1:]

"""
这个strong pruning 可以work的原因是我们的candidate_pool是所有的anagram, 而不是给你一个list里面包含一些candidate_pool 的情况，
所以127. Word Ladder那一题给了你一个possilbe candidates就不可以用这个pruning 了，同样433. Minimum Genetic Mutation给了你一个possilbe Gene bank,
所以也不可以用这个pruning
"""
