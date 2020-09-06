1302. Deepest Leaves Sum

Given a binary tree, return the sum of values of its deepest leaves.
 

Example 1:



Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15



"""
first dfs find the max depth, 2nd dfs get the sum of all nodes with max depth.
solution 2: level order bfs, 每次都在while循环里初始化max_depth_sums就可以保证输出的是最后一层的sums了，只需一次遍历
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
dfs find leaf and put it in the res
"""
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_depth = self._get_max_depth(root)
        return self._helper(root, 1, max_depth)
    
    def _get_max_depth(self, root):
        if not root:
            return 0
        return 1 + max(self._get_max_depth(root.left), self._get_max_depth(root.right))
    
    def _helper(self, root, curr_depth, max_depth):
        if not root:
            return 0
        if not root.left and not root.right and curr_depth == max_depth:
            return root.val
        
        left_sum = self._helper(root.left, curr_depth + 1, max_depth)
        right_sum = self._helper(root.right, curr_depth + 1, max_depth)
        
        return left_sum + right_sum
