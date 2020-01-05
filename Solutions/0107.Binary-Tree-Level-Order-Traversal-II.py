#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (49.26%)
# Likes:    954
# Dislikes: 179
# Total Accepted:    267.8K
# Total Submissions: 542.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its bottom-up level order traversal as:
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
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

"""solution 1: do a regular BFS then reverse the result"""
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = deque()
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                # 做两件事情：1. 将这一层的所有Node.val加入level中
                node = q.popleft()
                level.append(node.val)
                # 2. 将这一层的所有node的左右子树加入q中
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        
        i, j = 0, len(res) - 1
        while i < j:
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1

        return res
        
# @lc code=end

