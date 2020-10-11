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
class Solution(object):
    def findBottomLeftValue(self, root):
        self.max_level = 0
        self.res = root.val
        self._dfs(root, 0)
        return self.res
      
    def _dfs(self, root, curr_level):
        if not root:
            return
      
        if not root.left and not root.right:
            if curr_level > self.max_level:
                self.res = root.val
                self.max_level = curr_level
            return
      
        if root.left:                               # do dfs for left part first, 
            self._dfs(root.left, curr_level + 1)    # so that we can return the leftmost value in the last row
        if root.right:
            self._dfs(root.right, curr_level + 1)
            
            
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
