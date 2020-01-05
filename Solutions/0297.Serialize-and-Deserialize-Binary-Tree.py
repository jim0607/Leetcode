#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (44.24%)
# Likes:    2257
# Dislikes: 116
# Total Accepted:    252.4K
# Total Submissions: 569K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
# 
# Example: 
# 
# 
# You may serialize the following tree:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠    / \
# ⁠   4   5
# 
# as "[1,2,3,null,null,4,5]"
# 
# 
# Clarification: The above format is the same as how LeetCode serializes a
# binary tree. You do not necessarily need to follow this format, so please be
# creative and come up with different approaches yourself.
# 
# Note: Do not use class member/global/static variables to store states. Your
# serialize and deserialize algorithms should be stateless.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        # typical style for BFS
        res = ""
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                res += str(node.val) + ","
            else:
                res += "None,"
        
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        vals = data.split(",")

        root = TreeNode(int(vals[0]))
        q = deque()
        q.append(root)
        index = 1
        while q and index < len(vals):
            node = q.popleft()
            if vals[index] != "None":
                node.left = TreeNode(int(vals[index]))
                q.append(node.left)
            index += 1

            if vals[index] != "None":
                node.right = TreeNode(int(vals[index]))
                q.append(node.right)
            index += 1

        return root
                    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

