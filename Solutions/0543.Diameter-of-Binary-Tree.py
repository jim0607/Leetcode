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



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxDmtr = 0
        
        def maxDepth(root):
            """
            return the maxDepth of tree rooted as root
            """
            if not root:
                return 0
            
            leftDepth = maxDepth(root.left)
            rightDepth = maxDepth(root.right)
            
            self.maxDmtr = max(self.maxDmtr, leftDepth + rightDepth)    # 打个擂台吧
            
            rootDepth = max(leftDepth, rightDepth) + 1
            
            return rootDepth
        
                
        maxDepth(root)
        
        return self.maxDmtr



"""
Can somone tell me why this doesn't work?  
It doesn't work because the path may or may not pass through the root.
"""
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        return the diameter of tree rooted as root
        """
        if not root:
            return 0

        return self.maxDepth(root.left) + self.maxDepth(root.right)
        
    def maxDepth(self, root):
        """
        return the max depth of the tree rooted as root
        """
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        # divide
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        # merge
        depth = max(leftDepth, rightDepth) + 1
        
        return depth
