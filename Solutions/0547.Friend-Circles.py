"""
547. Friend Circles

There are N students in a class. Some of them are friends, while some are not. 
Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. 
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, 
then the ith and jth students are direct friends with each other, 
otherwise not. And you have to output the total number of friend circles among all the students.

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




"""
Solution 1: Union-Find O(MN). 
与LC 200 Nubmer of islands其实是同一题，只是这题给的是adjcency matrix representaion of a graph.
"""
class UnionFind:
    
    def __init__(self, n):
        self.father = collections.defaultdict(int)
        self.cnt = 0
        
        for i in range(n):
            self.add(i)
            
    def add(self, x):
        self.father[x] = x
        self.cnt += 1
        
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.cnt -= 1


class Solution:
    def findCircleNum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        uf = UnionFind(n)
        
        for i in range(n):
            for j in range(i, n):   # 题目给的是adjancency matrix, 只需要遍历adjacency matrix一半就可以了，因为如果1和3是朋友那么3和1也一定是朋友
                if matrix[i][j] == 1:
                    uf.union(i, j)
        
        return uf.cnt
       
       
       
       
       
"""
solution 2: dfs
"""
class Solution:
    def findCircleNum(self, matrix: List[List[int]]) -> int:
        # step 1: change the graph representation to be dictionary of adjacency list
        graph = collections.defaultdict(list)
        n = len(matrix)        
        for i in range(n):
            for j in range(i, n):  
                if matrix[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        
        def dfs(curr_i):
            visited.add(curr_i)
            for next_i in graph[curr_i]:
                if next_i not in visited:
                    dfs(next_i)        
        
        # step 2: dfs to visit each node
        cnt = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i)
                cnt += 1
                
        return cnt
