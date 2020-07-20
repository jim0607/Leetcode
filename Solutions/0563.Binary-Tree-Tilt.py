563. Binary Tree Tilt

Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input: 
         1
       /   \
      2     3
Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self._helper(root)[0]
        
    def _helper(self, root):
        if not root:
            return 0, 0     # return the tilt and the sum
        
        left_tilt, left_sum = self._helper(root.left)
        right_tilt, right_sum = self._helper(root.right)
        
        root_sum = left_sum + root.val + right_sum
        root_tilt = abs(left_sum - right_sum) + left_tilt + right_tilt
        
        return root_tilt, root_sum
