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

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 
        
        nums = []
        nums = self.inOrder(root)
        
        res = 0
        for num in nums:
            if L <= num <= R:
                res += num
                
        return res
    
    def inOrder(self, root):
        """return the list of inOrder traversal of BST with root as its root"""
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        res = []
        
        left = self.inOrder(root.left)
        right = self.inOrder(root.right)
        
        res += left
        res += [root.val]
        res += right
        
        return res
    

# solution 2: divide and conquer
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        
        # divide
        leftSum = self.rangeSumBST(root.left, L, R)
        rightSum = self.rangeSumBST(root.right, L, R)
        
        # conquer
        if root.val > R:
            return leftSum
        elif root.val < L:
            return rightSum
        else:
            return leftSum + rightSum + root.val
