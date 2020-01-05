#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#
# https://leetcode.com/problems/graph-valid-tree/description/
#
# algorithms
# Medium (40.90%)
# Likes:    811
# Dislikes: 27
# Total Accepted:    108.4K
# Total Submissions: 264.7K
# Testcase Example:  '5\n[[0,1],[0,2],[0,3],[1,4]]'
#
# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge
# is a pair of nodes), write a function to check whether these edges make up a
# valid tree.
# 
# Example 1:
# 
# 
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
# 
# Example 2:
# 
# 
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
# 
# Note: you can assume that no duplicate edges will appear in edges. Since all
# edges are undirected, [0,1] is the same as [1,0] and thus will not appear
# together in edges.
# 
#
"""判断图是不是一棵树（不一定非要是二叉树）需要满足两点：
1. 首先点的数目一定比边的数目多一个
2. 然后要确保no isolated node and no cycle，也即是保证每个点都能被访问且只被访问了一次，
也就是visited的数目要等于节点数目"""
# @lc code=start
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return Ture
        # 首先点的数目一定比边的数目多一个
        if len(edges) != n - 1:
            return False

        # 图的实现方法是使用hashmap，key是int表示节点, value是set(int)表示该节点所连接的相邻节点。
        neighbors = collections.defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        
        visited = {}
        from collections import deque
        q = deque()
        # 与二叉树的BFS相比多加了一行visited，每一次将一个node加入队列，都需要同时改变visited的值，就像是一对好基友
        q.append(0)
        visited[0] = True
        while q:
            currNode = q.popleft()
            visited[currNode] = True
            for node in neighbors[currNode]:  # 这里体现BFS，首先访问currNode节点的左右邻居节点
                # 如果已经访问过就不再访问了，这样可以保证每个节点都被访问过一次
                if node not in visited:  # 没访问过就加入队列同时改变visited的值（这两个操作是一对好基友）
                    q.append(node)
                    visited[node] = True
        
        return len(visited) == n  # 每个节点都被访问过且都被访问过一次

# @lc code=end

