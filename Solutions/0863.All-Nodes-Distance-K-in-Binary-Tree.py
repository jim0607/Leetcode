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
        graph = collections.defaultdict(list)
        def dfs(root):
            if not root:
                return
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        
        if not graph:
            return []
        
        # step 2: start from target, use bfs/dfs to find the nodes with distance == K
        q = collections.deque()
        q.append(target.val)
        visited = set()
        visited.add(target.val)
        
        level = -1
        res = []
        while q:
            lens = len(q)
            level += 1
            res = []
            for _ in range(lens):
                curr = q.popleft()
                res.append(curr)
                for next in graph[curr]:
                    if next not in visited:
                        q.append(next)
                        visited.add(next)
       
            if level == K:
                return res
            
        return []
        
        
"""
dfs 的写法
"""        
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # step 1: use dfs, change a tree to a graph with adjacency list representation
        graph = collections.defaultdict(list)
        def dfs(root):
            if not root:
                return
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)

        if not graph:
            return []

        # step 2: start from target, use bfs/dfs to find the nodes with distance == K
        def dfs_2(curr_node, curr_level):       # 带层序遍历，一定要把curr_level传进去
            # if not curr_node:     #  *****Bug: 注意不能用if not curr_node, 因为curr_node现在是数，可能等于0的******
            #     return
            
            if curr_level == K:
                res.append(curr_node)
            
            if curr_level > K:
                return
            
            for next_node in graph[curr_node]:
                if next_node not in visited:
                    visited.add(next_node)
                    dfs_2(next_node, curr_level + 1)
            
        res = []
        visited = set()
        visited.add(target.val)
        dfs_2(target.val, 0)
        
        return res
