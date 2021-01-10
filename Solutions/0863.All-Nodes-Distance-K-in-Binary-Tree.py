"""
863. All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""


"""
step 1: use dfs, change a tree to a graph with adjacency list representation; 
step 2: start from target, use bfs/dfs to find the nodes with distance == K
"""
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(curr_node):
            if not curr_node:
                return
            for next_node in [curr_node.left, curr_node.right]:
                if next_node:
                    graph[curr_node].append(next_node)
                    graph[next_node].append(curr_node)
                    dfs(next_node)
                    
                    
        def dfs2(curr_node, curr_dist):
            if curr_dist == K:
                res.append(curr_node.val)
                return
            for next_node in graph[curr_node]:
                if next_node not in visited:
                    visited.add(next_node)
                    dfs2(next_node, curr_dist + 1)
            
            
        graph = defaultdict(list)
        dfs(root)     # 第一个dfs用于建图
        res = []
        visited = set()
        for node in graph:
            if node == target:
                visited.add(node)
                dfs2(node, 0)
        return res


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # step 1: use dfs, change a tree to a graph with adjacency list representation
        def dfs(curr_node):
            if curr_node.left:
                graph[curr_node.val].append(curr_node.left.val)
                graph[curr_node.left.val].append(curr_node.val)
                dfs(curr_node.left)
            if curr_node.right:
                graph[curr_node.val].append(curr_node.right.val)
                graph[curr_node.right.val].append(curr_node.val)
                dfs(curr_node.right)
                
                
        # step 2: start from target, use bfs/dfs to find the nodes with distance == K
        def bfs():
            q = deque()
            visited = set()
            q.append(target.val)
            visited.add(target.val)
            
            dist = -1
            while len(q) > 0:
                dist += 1
                if dist == K:
                    return list(q)
                
                lens = len(q)
                for _ in range(lens):
                    curr_node = q.popleft()
                    for next_node in graph[curr_node]:
                        if next_node not in visited:
                            q.append(next_node)
                            visited.add(next_node)
            return []
                

        graph = defaultdict(list)
        dfs(root)
        return bfs()
