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

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        res = []
        q = collections.deque()             # q 里面放的是TreeNode
        q.append(root)
        while q:
            level = []
            lens = len(q)
            for _ in range(lens):
                curr = q.popleft()
                if curr:
                    level.append(str(curr.val))
                    q.append(curr.left)
                    q.append(curr.right)
                else:
                    level.append("#")       # "#" means None

            res += level

        return ",".join(res)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        res = data.split(",")
        idx = 0
        root = TreeNode(res[idx])
        idx += 1
        q = collections.deque()     # q 里面放的是TreeNode, q 里面永远都放TreeNode, 放别的没有意义呀，list可以通过idx进行查询呀！
        q.append(root)
        while q and idx < len(res):
            curr_node = q.popleft()
            if res[idx] == "#":
                curr_node.left = None
            else:
                curr_node.left = TreeNode(res[idx])
                q.append(curr_node.left)
            idx += 1        # 注意index不要写到if里面，因为vals[index]==None的情况下，我们也需要将index往前进一步

            if res[idx] == "#":
                curr_node.right = None
            else:
                curr_node.right = TreeNode(res[idx])
                q.append(curr_node.right)
            idx += 1

        return root
    
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
