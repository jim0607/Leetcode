#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (44.47%)
# Likes:    1434
# Dislikes: 83
# Total Accepted:    287.4K
# Total Submissions: 644.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
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
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
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

"""这是102 中序遍历的小小改变，依然用BFS"""
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = deque()
        q.append(root)
        reverse = False
        while q:
            level = []
            lens = len(q)
            for _ in range(lens):
                # 做两件事：1. 把这一层所有的node.val放进level
                node = q.popleft()
                level.append(node.val)
                # 2. 把这一层所有的node的左右节放进q
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if reverse:
                res.append(level[::-1])
            else:
                res.append(level)
            reverse = not reverse
            
        return res

# @lc code=end

