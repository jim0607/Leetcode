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


# this is definetely a hard problem
# https://leetcode.com/problems/delete-node-in-a-bst/solution/
"""
O(height), O(height)
"""
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # case 1: if root is leaf node - just delete it
            if not root.left and not root.right:
                root = None
            
            # case 2: if root has right node - replace the root by the successor,
            # and then delete the successor in the right subtree root.right = deleteNode(root.right, root.val)
            elif root.right:
                root.val = self._successor(root)
                root.right = self.deleteNode(root.right, root.val)
            
            # case 3: if root has no right node - replace the root by the predessor
            # and then delete the predecessor in the left subtree root.left = deleteNode(root.left, root.val)
            else:
                root.val = self._predessor(root)
                root.left = self.deleteNode(root.left, root.val)
        
        return root
        
    def _successor(self, root):     # O(height), 因为一直都在往下走
        """
        Return the successor of the root by taking one step right and always left, cuz the successor is the node just larger than the root
        """
        curr = root.right
        while curr.left:
            curr = curr.left
        return curr.val
    
    def _predessor(self, root):
        """
        Return the predecessor of the root by taking one step left and then always right
        """
        curr = root.left
        while curr.right:
            curr = curr.right
        return curr.val




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                predessor = self.findMax(root.left)
                root.val = predessor.val
                root.left = self.deleteNode(root.left, predessor.val)
                
        return root
    
    def findMax(self, root):
        while root.right:
            root = root.right
            
        return root
