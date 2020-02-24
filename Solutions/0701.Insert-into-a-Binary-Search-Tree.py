#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
#
# algorithms
# Medium (78.04%)
# Likes:    548
# Dislikes: 59
# Total Accepted:    75.2K
# Total Submissions: 96.3K
# Testcase Example:  '[4,2,7,1,3]\n5'
#
# Given the root node of a binary search tree (BST) and a value to be inserted
# into the tree, insert the value into the BST. Return the root node of the BST
# after the insertion. It is guaranteed that the new value does not exist in
# the original BST.
# 
# Note that there may exist multiple valid ways for the insertion, as long as
# the tree remains a BST after insertion. You can return any of them.
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
# And the value to insert: 5
# 
# 
# You can return this binary search tree:
# 
# 
# ⁠        4
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   /
# ⁠   1   3 5
# 
# 
# This tree is also valid:
# 
# 
# ⁠        5
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   
# ⁠   1   3
# ⁠        \
# ⁠         4
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# One of the huge BST advantages is a search for arbitrary element in O(logN) time. Here we'll see that the insert time is O(logN), too, in the average case.
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """insert a node into a tree rooted as root, return the root"""
        
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)    # 更新root.right
        
        else:
            root.left = self.insertIntoBST(root.left, val)
        
        return root
            
# @lc code=end

"""Time complexity : O(H), where H is a tree height. That results in O(logN) in the average case, and O(N) in the worst case.
Space complexity : O(H) to keep the recursion stack, i.e. O(logN) in the average case, and O(N) in the worst case."""
