"""
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively.
"""


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(root):
            """
            return the root with left and right flipped
            """
            if not root:
                return None
            
            left_flp = helper(root.left)
            right_flp = helper(root.right)
            
            root.left = right_flp
            root.right = left_flp
            
            return root
        
        
        if not root:
            return True
        
        left_root = root.left
        right_flp = helper(root.right)
        return self.equal(left_root, right_flp)
    
    def equal(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        
        left_eq = self.equal(root1.left, root2.left)
        right_eq = self.equal(root1.right, root2.right)
        
        return left_eq and right_eq
