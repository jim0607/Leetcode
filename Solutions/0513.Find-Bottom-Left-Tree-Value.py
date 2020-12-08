"""
513. Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
"""

"""
dfs
"""
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def dfs(curr_node, curr_depth):
            if curr_depth == depth:
                self.res = curr_node.val
                return
            
            for next_node in [curr_node.right, curr_node.left]:     # do right node first
                if next_node:
                    dfs(next_node, curr_depth + 1)

        
        depth = self.find_depth(root)
        self.res = 0
        dfs(root, 1)
        return self.res
    
    
    def find_depth(self, root):
        if not root:
            return 0
        
        return 1 + max(self.find_depth(root.left), self.find_depth(root.right))
            
            
"""
bfs
"""
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        bottom_left = root.val
        q = collections.deque()
        q.append(root)
        while len(q) > 0:
            curr_node = q.popleft()
            bottom_left = curr_node.val
            if curr_node.right:         # right first, then left
                q.append(curr_node.right)
            if curr_node.left:
                q.append(curr_node.left)
        return bottom_left
