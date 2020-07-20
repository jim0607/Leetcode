156. Binary Tree Upside Down

Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

Example:

Input: [1,2,3,4,5]

    1
   / \
  2   3
 / \
4   5

Output: return the root of the binary tree [4,5,2,#,#,3,1]

   4
  / \
 5   2
    / \
   3   1  
Clarification:

Confused what [4,5,2,#,#,3,1] means? Read more below on how binary tree is serialized on OJ.

The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

Here's an example:

   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as [1,2,3,#,#,4,#,#,5].


"""
没明白题目啥意思，大概就是一通左右连接的操作吧，题目描述真差劲哦
https://leetcode.com/problems/binary-tree-upside-down/discuss/468607/Clarification-of-the-problem-description
"""
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root or (not root.left and not root.right):
            return root
        
        new_root = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.right, root.left = None, None
        
        return new_root
