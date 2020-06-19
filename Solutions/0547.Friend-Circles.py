547. Friend Circles

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.


"""
Solution 1: Union-Find O(MN)
"""
class UnionFind:
    def __init__(self, size):
        self.father = collections.defaultdict()
        self.disjoint_cnt = 0
        
        for i in range(size):
            self.father[i] = i
            self.disjoint_cnt += 1
        
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = self.father[root_b]
            self.disjoint_cnt -= 1
    
    
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(M), len(M[0])
        uf = UnionFind(m)
        for i in range(m):
            for j in range(i + 1, n):   # 只需要遍历adjacency matrix一半就可以了，因为如果1和3是朋友那么3和1也一定是朋友
                if M[i][j] == 1:
                    uf.union(i, j)
                    
        return uf.disjoint_cnt
