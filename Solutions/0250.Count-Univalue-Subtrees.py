250. Count Univalue Subtrees

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.cnt = 0
        
        def isUnivalTree(root):
            """
            return if the tree is a univalTree?
            """
            if not root:
                return True
            if not root.left and not root.right:
                self.cnt += 1
                return True
            
            rightIsUnivalTree = isUnivalTree(root.right)
            leftIsUnivalTree = isUnivalTree(root.left)
            
            if not root.left:
                if rightIsUnivalTree and root.val == root.right.val:
                    self.cnt += 1
                    return True
                else:
                    return False
                
            if not root.right:
                if leftIsUnivalTree and root.val == root.left.val:
                    self.cnt += 1
                    return True
                else:
                    return False
            
            if leftIsUnivalTree and rightIsUnivalTree and root.val == root.left.val and root.val == root.right.val:
                self.cnt += 1
                return True
            
        isUnivalTree(root)
        
        return self.cnt
