"""
549. Binary Tree Longest Consecutive Sequence II

Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. 
For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. 
On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
 

Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
"""

        
        
"""
helper function returns (the LCS ended with root decreasing, increasing, without root, pass root)
"""
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        return max(self._helper(root))
        
        
    def _helper(self, root):
        """
        Return the LCS ended with root decreasing/increasing, without root, pass root
        """
        if not root:
            return 0, 0, 0, 0
        if not root.left and not root.right:
            return 1, 1, 0, 1
        
        left_w_dec, left_w_inc, left_wo, left_p = self._helper(root.left)
        right_w_dec, right_w_inc, right_wo, right_p = self._helper(root.right)
        
        root_wo = max(left_w_dec, left_w_inc, left_wo, left_p, right_w_dec, right_w_inc, right_wo, right_p)
        
        root_w_inc, root_w_dec = 1, 1
        if root.left and root.left.val == root.val + 1:
            root_w_inc = max(root_w_inc, left_w_inc + 1)
        if root.right and root.right.val == root.val + 1:
            root_w_inc = max(root_w_inc, right_w_inc + 1)
        if root.left and root.left.val == root.val - 1:
            root_w_dec = max(root_w_dec, left_w_dec + 1)
        if root.right and root.right.val == root.val - 1:
            root_w_dec = max(root_w_dec, right_w_dec + 1)
            
        root_p = 1
        if root.left and root.right and root.val == root.left.val - 1 == root.right.val + 1:
            root_p = max(root_p, 1 + left_w_inc + right_w_dec)
        if root.left and root.right and root.val == root.left.val + 1 == root.right.val - 1:
            root_p = max(root_p, 1 + left_w_dec + right_w_inc)

        return root_w_dec, root_w_inc, root_wo, root_p
        

        


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.res = 1
        self.helper(root)
        
        return self.res
        
    def helper(self, root):
        """
        return the LCS_increasing and LCS_decreasing started with root
        """
        if not root:
            return (0, 0)
        
        left_increasing, left_decreasing = self.helper(root.left)
        right_increasing, right_decreasing = self.helper(root.right)
        
        root_increasing, root_decreasing = 1, 1
        
        if root.left:
            if root.left.val == root.val + 1:
                root_increasing = max(root_increasing, left_increasing + 1)
            elif root.left.val == root.val - 1:
                root_decreasing = max(root_decreasing, left_decreasing + 1)
                
        if root.right:
            if root.right.val == root.val + 1:
                root_increasing = max(root_increasing, right_increasing + 1)
            elif root.right.val == root.val - 1:
                root_decreasing = max(root_decreasing, right_decreasing + 1)

        self.res = max(self.res, root_increasing + root_decreasing - 1)
        
        return (root_increasing, root_decreasing)
