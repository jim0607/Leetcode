543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.



class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.max_dia = 0
        self._get_depth(root)
        
        return self.max_dia
    
    def _get_depth(self, root):
        if not root:
            return 0
        
        left_depth = self._get_depth(root.left)
        right_depth = self._get_depth(root.right)
        
        self.max_dia = max(self.max_dia, left_depth + right_depth)  # 打个擂台吧
        
        return max(left_depth, right_depth) + 1



"""
Can somone tell me why this doesn't work?  
It doesn't work because the path may or may not pass through the root.
把这个例子放到leetcode中用Tree Visualizer看一看就知道为什么了[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
因为可能root.left只有一个节点，而root.right有很多节点，这很多个节点中可能有很多左节点，所以max_diameter只发生在root的右半边
"""
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return self._get_depth(root.left) + self._get_depth(root.right)
    
    def _get_depth(self, root):
        if not root:
            return 0
        
        left_depth = self._get_depth(root.left)
        right_depth = self._get_depth(root.right)
        
        return max(left_depth, right_depth) + 1
