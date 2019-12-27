#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#
# https://leetcode.com/problems/range-sum-of-bst/description/
#
# algorithms
# Easy (78.71%)
# Likes:    678
# Dislikes: 142
# Total Accepted:    131.6K
# Total Submissions: 167.2K
# Testcase Example:  '[10,5,15,3,7,null,18]\n7\n15'
#
# Given the root node of a binary search tree, return the sum of values of all
# nodes with value between L and R (inclusive).
# 
# The binary search tree is guaranteed to have unique values.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32
# 
# 
# 
# Example 2:
# 
# 
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree is at most 10000.
# The final answer is guaranteed to be less than 2^31.
# 
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

# solution 1: store all the nodes in a sortedArr by in-order traverse
# class Solution:
#     sortedArr = []
#     def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
#         if not root:
#             return 0
#         self._inOrder_(root)
#         # print(self.sortedArr)
#         sumNodes = 0
#         if self.sortedArr[-1] < L or self.sortedArr[0] > R:
#             return 0
#         for node in self.sortedArr:
#             if L <= node <= R:
#                 sumNodes += node
#         return sumNodes 
    
#     def _inOrder_(self, root: TreeNode):
#         """
#         in-order traverse the tree and put the nodes in sortedArr, no return
#         """
#         if not root:
#             return
#         self._inOrder_(root.left)
#         self.sortedArr.append(root.val)
#         self._inOrder_(root.right)

# solution 2: divide and conquer
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        return self._divideAndConquer_(root, L, R, 0)

    def _divideAndConquer_(self, root: TreeNode, L: int, R: int, sumNodes: int) -> int:
        """
        divide and conquer to return the sum for nodes in range L-R under root
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val if L <= root.val <= R else 0

        # divide 
        left = self._divideAndConquer_(root.left, L, R, sumNodes)
        right = self._divideAndConquer_(root.right, L, R, sumNodes)

        # conquer - if root < L then go to right, if root > R then go to left, else return (go left+go right + root.val)
        if root.val < L:
            return right
        elif root.val > R:
            return left
        else:
            return left + right + root.val
        
# @lc code=end

