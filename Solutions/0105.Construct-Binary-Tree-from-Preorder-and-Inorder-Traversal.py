105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
   
   
   
"""
solution 1: simple recursion - O(N^2)
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        
        root = TreeNode()
        root.val = preorder.pop(0)  # this takes O(N), so overall the algorithm takes O(N^2)
        
        # find the index where root.val is in inorder list
        # this takes O(N), so overall the algorithm takes O(N^2)
        idx = 0         
        for i, num in enumerate(inorder):
            if num == root.val:
                idx = i
                break
            
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
        
        return root
        
        
        
"""
solution 2: O(N) - 没看明白，各大博主无人提及O(N)的解法
"""
争取看懂解答！
"""

