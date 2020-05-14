Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

""" Time complexity O(N) """
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if root == p or root == q:
            return root
        
        # divide 
        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)
        
        # conquer
        if leftLCA is not None and rightLCA is not None:    # meaning find one node in the left and the other node in the right
            return root
        elif leftLCA is not None:
            return leftLCA
        elif rightLCA is not None:
            return rightLCA
        
        

"""
Solution 2: very slow O(N^2), but work fine
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return 
        
        if self.isUnderRoot(root.left, p) and self.isUnderRoot(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        
        if self.isUnderRoot(root.right, p) and self.isUnderRoot(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        
        else:
            return root
        
        
    def isUnderRoot(self, root, n):
        if not root:
            return False
        
        isUnderLeft = self.isUnderRoot(root.left, n)
        isUnderRight = self.isUnderRoot(root.right, n)
        
        return isUnderLeft or isUnderRight or root.val == n.val
