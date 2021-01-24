"""
839. Similar String Groups

Two strings X and Y are similar if we can swap two letters (in different positions) of X, 
so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), 
and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  
Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list A of strings.  Every string in A is an anagram of every other string in A.  
How many groups are there?

 
Example 1:

Input: A = ["tars","rats","arts","star"]
Output: 2
"""


"""
can use bfs/dfs/union-find to traverse the graph.
since we want to output disconnected components, union-find is quite straight forward - O(L*N^2)
"""
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        uf = UnionFind(A)
        for i in range(len(A)-1):       # 这种两两相邻的node相互比较的思想非常重要
            for j in range(i+1, len(A)):
                if uf.connected(A[i], A[j]):
                    continue
                if self._is_similar(A[i], A[j]):
                    uf.union(A[i], A[j])
        return uf.cnt
    
    def _is_similar(self, s, t):  # 利用了s1和s2是anagram的前提将复杂度降为O(L)
        diff_cnt = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                diff_cnt += 1
            if diff_cnt > 2:
                return False
        return True
    
    
class UnionFind:
    
    def __init__(self, A):
        self.father = collections.defaultdict(str)
        self.cnt = 0
        
        for s in A:
            if s not in self.father:   # 注意这里的判断至关重要
                self.add(s)            # 因为如果A中有重复的话cnt += 1不能做两次
                
    def add(self, x):
        self.father[x] = x
        self.cnt += 1
    
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])    # path compression
        return self.father[x]
    
    def connected(self, a, b):
        return self.find(a) == self.find(b)
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.cnt -= 1
