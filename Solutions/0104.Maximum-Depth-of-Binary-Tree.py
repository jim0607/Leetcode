Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# solution 1: divide and conquer
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if not root:
            return 0
        
        # divide
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        # conquer
        depth = max(left, right) + 1
        
        return depth
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# solution 2: traverse
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        global depth
        depth = 0
        self.maxDepthHelper(root, 1)
        
        return depth
        
    # different with divide and conquer method, traverse does not have a return value
    def maxDepthHelper(self, root: TreeNode, currDepth):
        if not root:
            return
        
        global depth
        if currDepth > depth:
            depth = currDepth

        self.maxDepthHelper(root.left, currDepth + 1)
        self.maxDepthHelper(root.right, currDepth + 1)
