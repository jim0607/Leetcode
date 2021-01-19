"""
947. Most Stones Removed with Same Row or Column

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing all the stones that share column or row.

What is the largest possible number of moves we can make?

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Example 3:

Input: stones = [[0,0]]
Output: 0
"""


"""
可以remove的个数是 n - disjoint_cnt
"""
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UnionFind(n)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)
        return n - uf.disjoint_cnt
    

class UnionFind:
    
    def __init__(self, n):
        self.father = defaultdict(int)
        self.disjoint_cnt = 0
        
        for x in range(n):
            self.add(x)
    
    def add(self, x):
        if x not in self.father:
            self.father[x] = x
            self.disjoint_cnt += 1
                
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.disjoint_cnt -= 1



"""
Use two for loops to compare each pos with another pos in the list, if two positions share same row or col,
then we should union them, each time there is a union, it means we can do one removal, then we set cnt += 1
"""
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind(stones)
        for i in range(len(stones) - 1):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(tuple(stones[i]), tuple(stones[j]))
        return uf.cnt
    
    
class UnionFind:
    
    def __init__(self, stones):
        self.father = collections.defaultdict(tuple)
        self.cnt = 0
        
        for stone in stones:
            self.father[tuple(stone)] = tuple(stone)
            
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.cnt += 1
        

"""
The improved DSU solution creates a map of all the nodes with a certain X coordinate
and a second map with all the nodes with a Y coordinate. 
This allows us to quickly join all of a node's neighbour into a set. 
This improves the naïve DSU implementation from O(n^2) to O(n)!!
Algorithm: when we see a stone that appears in a row or a column at the first time, 
we define this stone as the parent of this row and column, 
next time we see a new stone, just union it with its parent, which stores in the hashmap, 
thus we can do it in one pass.
Very cool!!
"""
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind(stones)
        
        rowmap = defaultdict(tuple)
        colmap = defaultdict(tuple)
        
        for x, y in stones:
            if x not in rowmap:
                rowmap[x] = (x, y)
            if y not in colmap:
                colmap[y] = (x, y)
            
            uf.union((x, y), rowmap[x])
            uf.union((x, y), colmap[y])
            
        return uf.cnt
    
    
class UnionFind:
    
    def __init__(self, stones):
        self.father = defaultdict(tuple)
        self.cnt = 0        # how many union performed (or how many move we can perform)
        for i, j in stones:
            self.father[(i, j)] = (i, j)
            
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.cnt += 1
