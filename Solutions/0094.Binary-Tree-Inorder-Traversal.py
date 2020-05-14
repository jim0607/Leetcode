#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (59.91%)
# Likes:    2259
# Dislikes: 96
# Total Accepted:    588.3K
# Total Submissions: 981.7K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# trivial solution using recursion
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        
        leftRes = self.inorderTraversal(root.left)
        res += leftRes
        
        res.append(root.val)
        
        rightRes = self.inorderTraversal(root.right)
        res += rightRes
        
        return res
        
# @lc code=end


# solution using recursion is trivial, we should memorize the iterative solution using stack
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack, res = [], []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)  # push is append for a stack implemented by list
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            # very important sentence, should memorize
            curr = curr.right

        return res
