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

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        res = []
        q = deque()
        q.append(root)
        while len(q) > 0:
            level = []
            lens = len(q)     # 层序遍历  
            for _ in range(lens):
                curr_node = q.popleft()
                if curr_node:
                    level.append(str(curr_node.val))
                    q.append(curr_node.left)
                    q.append(curr_node.right)
                else:
                    level.append("#")       # we use "#" to represent None
            
            res += level
                
        return ",".join(res)        # [1, 2, 3, #, #, 4, 5]
            
    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        s = data.split(",")
        root = TreeNode(int(s[idx]))
        idx = 1
        
        q = collections.deque()
        q.append(root)          # q 里面永远都放TreeNode, 永远永远！
        while len(q) > 0:
            curr_node = q.popleft()
            
            # step 1: assign s[idx] to curr_node.left
            if s[idx] == "#":
                curr_node.left = None
            else:
                curr_node.left = TreeNode(int(s[idx]))
                q.append(curr_node.left)
                
            idx += 1    # 注意index不要写到if里面，
                        # 因为vals[index]==None的情况下，我们也需要将index往前进一步
            # step 2: assign s[idx+1] to curr_node.right
            if s[idx] == "#":
                curr_node.right = None
            else:
                curr_node.right = TreeNode(int(s[idx]))
                q.append(curr_node.right)
                
            idx += 1
            
        return root
