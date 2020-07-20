685. Redundant Connection II

In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3
Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.



"""
First, go through the edges and detect if any node has two parents, i.e., if there exist two edges pointing to the same node. 
If there exists such two edges, record them as cand1 and cand2, because we know one of them must be the answer. 
If there do not exist such two edges, then cand1, cand2 will be None and there must be a cycle in the graph.
Just pretend the edges are undirected. Then go through the edges and do a regular union find, 
which can detect the existence of a cycle in an undirected graph. 
(Ignore the existence of cand2 when going through the edges, i.e., if [node1, node2] == cand2: continue)
第一种：无环，但是有结点入度为2的结点（结点3）
[[1,2], [1,3], [2,3]]
  1
 / \
v   v
2-->3
If there is no cycle, then we know cand2 must exist and it is the bad edge we are looking for.
Here we return [2, 3]
第二种：有环，没有入度为2的结点
[[1,2], [2,3], [3,4], [4,1], [1,5]]
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
If there is a cycle and cand1, cand2 are not found, 
then the edge that incurs the cycle (the current edge when we go through the edges) is the bad edge.
Here we return [4, 1]
第三种：有环，且有入度为2的结点（结点1）
[[1,2],[2,3],[3,1],[4,1]]
     4
    /
   v
   1
 /  ^
v    \
2 -->3
If there is a cycle and cand1, cand2 are found, then cand1 must be already in the cycle and it is the bad edge. 不懂！
尼玛cand1, cand2是哪一个不是根据你的遍历的顺序决定的么?
Here we return [3, 1]. 
"""
class UnionFind:
    
    def __init__(self, edges):
        self.father = collections.defaultdict()     # O(E)
        for a, b in edges:
            self.father[a] = a
            self.father[b] = b
            
    def find(self, x):
        if self.father[x] == x:
            return x
        
        self.father[x] = self.find(self.father[x])
        
        return self.father[x]
    
    def connected(self, a, b):
        return self.find(a) == self.find(b)
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # step 1: First, go through the edges and detect if any node has two parents, 
        # i.e., if there exist two edges pointing to the same node. 
        cand1, cand2 = None, None
        pointed_at = {}
        for n1, n2 in edges:
            if n2 in pointed_at:
                cand1, cand2 = pointed_at[n2], [n1, n2]
                break
            pointed_at[n2] = [n1, n2]
        
        # step 2: Then go through the edges and do a regular union find, 
        # which can detect the existence of a cycle in an undirected graph.
        uf = UnionFind(edges)
        for a, b in edges:          # O(E)
            if (a, b) == cand2:     # we ignore cand2 when we go through the edges
                continue
            if uf.connected(a, b):
                if cand1: return cand1
                return [a, b]
            uf.union(a, b)
        return cand2
