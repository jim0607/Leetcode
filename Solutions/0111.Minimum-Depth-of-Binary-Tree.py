#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (36.30%)
# Likes:    968
# Dislikes: 554
# Total Accepted:    352.5K
# Total Submissions: 969.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its minimum depth = 2.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth = 0
        q = deque()
        q.append(root)
        while q:
            lens = len(q)
            depth += 1
            for _ in range(lens):
                # 做两件事：1. 判断这一层的所有的Node是不是遇到同时没有左右儿子的节点，如果遇到说明这里就是最小深度了
                node = q.popleft()
                if not node.left and not node.right:    # 此时为叶子节点
                   return depth
                # 2. 把这一层所有的node的左右节点放进q
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return depth
        

"""solution 2: recursion"""
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """return the min depth of Binary Tree rooted as root"""
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        if not root.left:
            return self.minDepth(root.right) + 1
        
        if not root.right:
            return self.minDepth(root.left) + 1
        
        else:
            leftMin = self.minDepth(root.left)
            rightMin = self.minDepth(root.right)
            return min(leftMin, rightMin) + 1
