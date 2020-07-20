404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sums = 0
        self._helper(root)
        return self.sums
    
    def _helper(self, root):
        if not root:
            return
        
        if root.left:
            left_node = root.left
            if not left_node.left and not left_node.right:
                self.sums += root.left.val
            self._helper(root.left)
            
        if root.right:
            self._helper(root.right)
