#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
#
# algorithms
# Easy (69.98%)
# Likes:    457
# Dislikes: 104
# Total Accepted:    97.7K
# Total Submissions: 139.6K
# Testcase Example:  '[4,2,7,1,3]\n2'
#
# Given the root node of a binary search tree (BST) and a value. You need to
# find the node in the BST that the node's value equals the given value. Return
# the subtree rooted with that node. If such node doesn't exist, you should
# return NULL.
# 
# For example, 
# 
# 
# Given the tree:
# ⁠       4
# ⁠      / \
# ⁠     2   7
# ⁠    / \
# ⁠   1   3
# 
# And the value to search: 2
# 
# 
# You should return this subtree:
# 
# 
# ⁠     2     
# ⁠    / \   
# ⁠   1   3
# 
# 
# In the example above, if we want to search the value 5, since there is no
# node with value 5, we should return NULL.
# 
# Note that an empty tree is represented by NULL, therefore you would see the
# expected output (serialized tree format) as [], not null.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# the problem is not clear, it's actually asking for returning the node, 
# for searching BST, we can use divide and conquer
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if not root.left and not root.right:
            return root if root.val == val else None
        # divide
        left = self.searchBST(root.left, val)
        right = self.searchBST(root.right, val)

        # conquer
        if val == root.val:
            return root
        elif val < root.val:
            return left
        else:
            return right
        

# @lc code=end

