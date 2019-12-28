#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#
# https://leetcode.com/problems/delete-node-in-a-bst/description/
#
# algorithms
# Medium (41.25%)
# Likes:    1261
# Dislikes: 69
# Total Accepted:    85.8K
# Total Submissions: 207.8K
# Testcase Example:  '[5,3,6,2,4,null,7]\n3'
#
# Given a root node reference of a BST and a key, delete the node with the
# given key in the BST. Return the root node reference (possibly updated) of
# the BST.
# 
# Basically, the deletion can be divided into two stages:
# 
# Search for a node to remove.
# If the node is found, delete the node.
# 
# 
# 
# Note: Time complexity should be O(height of tree).
# 
# Example:
# 
# root = [5,3,6,2,4,null,7]
# key = 3
# 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Given key to delete is 3. So we find the node with value 3 and delete it.
# 
# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
# 
# ⁠   5
# ⁠  / \
# ⁠ 4   6
# ⁠/     \
# 2       7
# 
# Another valid answer is [5,2,6,null,4,null,7].
# 
# ⁠   5
# ⁠  / \
# ⁠ 2   6
# ⁠  \   \
# ⁠   4   7
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

# this is definetely a hard problem
# https://leetcode.com/problems/delete-node-in-a-bst/solution/
class Solution:
    def successor(self, root: TreeNode) -> int:
        """
        return the successor of the root by taking one step right and always left, cuz the 
        successor is the node just larger than the root
        """
        if not root:
            return None
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root: TreeNode) -> int:
        """
        return the predecessor of the root by taking one step left and then always right
        """
        if not root:
            return None
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        # delete the root
        else:
            # if node is a leaf, simply delete it
            if not root.left and not root.right:
                root = None
            # If the node is not a leaf and has the right child, then replace the node value by a successor value root.val = successor.v
            # and then recursively delete the successor in the right subtree root.right = deleteNode(root.right, root.val).
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # If the node is not a leaf and has only the left child, then replace the node value by a predecessor value root.val = predecessor.val, 
            # and then recursively delete the predecessor in the left subtree root.left = deleteNode(root.left, root.val).
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root
        
# @lc code=end

