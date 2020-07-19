222. Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6



"""
solution 1: dfs to visit every node
"""
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return
            self.cnt += 1
            dfs(root.left)
            dfs(root.right)
        
        self.cnt = 0
        dfs(root)
        return self.cnt
        
        
"""
solution 2: use the property of complete Tree - O(logN*logN)
Case 1: If left sub tree height equals right sub tree height then:
left subtree is a perfect binary tree, but right subtree may or may not
    1
   / \
  2   3
 / \  /\
4  5 6
Case 2: If left sub tree height greater than right sub tree height then:
# right subtree is a perfect binary tree, but left subTree may or may not

    1
   / \
  2   3
 / \ / \
4   
"""
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_depth = self._depth(root.left)
        right_depth = self._depth(root.right)
        
        if left_depth == right_depth:       # left subtree is a perfect binary tree, but right subtree may or may not
            return 2 ** self._depth(root.left) + self.countNodes(root.right)
        elif left_depth > right_depth:      # right subtree is a perfect binary tree, but left subTree may or may not
            return 2 ** self._depth(root.right) + self.countNodes(root.left)
        
    def _depth(self, root):
        if not root:
            return 0
        
        return 1 + self._depth(root.left)  
