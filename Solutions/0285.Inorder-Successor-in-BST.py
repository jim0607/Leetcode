#
# @lc app=leetcode id=285 lang=python3
#
# [285] Inorder Successor in BST
#
# https://leetcode.com/problems/inorder-successor-in-bst/description/
#
# algorithms
# Medium (37.45%)
# Likes:    890
# Dislikes: 55
# Total Accepted:    127.5K
# Total Submissions: 340.4K
# Testcase Example:  '[2,1,3]\n1'
#
# Given a binary search tree and a node in it, find the in-order successor of
# that node in the BST.
# 
# The successor of a node p is the node with the smallest key greater than
# p.val.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [2,1,3], p = 1
# Output: 2
# Explanation: 1's in-order successor node is 2. Note that both p and the
# return value is of TreeNode type.
# 
# 
# Example 2:
# 
# 
# Input: root = [5,3,6,2,4,null,null,1], p = 6
# Output: null
# Explanation: There is no in-order successor of the current node, so the
# answer is null.
# 
# 
# 
# 
# Note:
# 
# 
# If the given node has no in-order successor in the tree, return null.
# It's guaranteed that the values of the tree are unique.
# 
# 
#

"""solution 2. divide and conquer
solution 1 is easy to understand, but it costs extra space to store all the nodes"""
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if root.val > p.val:
            left = self.inorderSuccessor(root.left, p)
            return left if left else root   # if not left, that means p is the largest node on the left
        
        else:
            return self.inorderSuccessor(root.right, p)
        

"""solution 1: in-order traverse"""
class Solution:
    # a list of TreeNode
    inOrderArr = []
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        self._inOrder_(root)
        if p == self.inOrderArr[-1]:
            return None
        for i, node in enumerate(self.inOrderArr):
            if node == p:
                return self.inOrderArr[i + 1]

    def _inOrder_(self, root: "TreeNode"):
        """
        in order traverse the tree, and put the nodes value in the arr
        """
        if not root:
            return
        self._inOrder_(root.left)
        self.inOrderArr.append(root)
        self._inOrder_(root.right)

# @lc code=en
