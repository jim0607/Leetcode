687. Longest Univalue Path

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

 

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

 

Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2

 

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.



"""
在binary tree里求longest path问题，如果任何path都算数的话，那么我们在divide and conquer的时候要分成两种情况讨论：
1. path ended with root; 2: path not ended with root
我们往往需要在helper函数中返回end_w和end_wo两种情况的值
"""
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        max_w, max_wo = self._dfs(root)
        return max(max_w, max_wo) - 1
        
    def _dfs(self, root):
        if not root:
            return 0, 0
        
        # divide
        left_max_w, left_max_wo = self._dfs(root.left)      # ended with, and not ended with root.left
        right_max_w, right_max_wo = self._dfs(root.right)
        
        # 更新root_max_w
        root_max_w = 1
        if root.left and root.val == root.left.val:
            root_max_w = max(left_max_w + 1, root_max_w)
        if root.right and root.val == root.right.val:
            root_max_w = max(right_max_w + 1, root_max_w)   # 注意要用max去更新
            
        # 更新root_max_wo
        left_max = max(left_max_w, left_max_wo)
        right_max = max(right_max_w, right_max_wo)
        root_max_wo = max(left_max, right_max)
        if root.left and root.right and root.val == root.left.val and root.val == root.right.val:
            root_max_wo = max(left_max_w + right_max_w + 1, root_max_wo)
            
        return root_max_w, root_max_wo
