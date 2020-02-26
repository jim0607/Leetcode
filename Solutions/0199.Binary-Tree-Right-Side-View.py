#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (50.79%)
# Likes:    1529
# Dislikes: 78
# Total Accepted:    219.4K
# Total Submissions: 431.2K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# 
# Example:
# 
# 
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""其实是在找层序遍历中的最后一个元素，层序遍历用BFS"""
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque()
        q.append(root)
        while q:
            lens = len(q)
            for _ in range(lens):
                # 做两件事情：1. 找到每一层所有Node中最右边的那一个
                node = q.popleft()
                rightMostVal = node.val
                # 2. 将这一层中所有的node的左右节点分别入队列
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(rightMostVal)
            
        return res
        
# @lc code=end

