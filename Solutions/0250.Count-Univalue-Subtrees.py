250. Count Univalue Subtrees

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4



"""
root is a univalue subtree if left is and right is and root.val = left.val = right.val;
heper function returns (is root a univalue subtree, cnt of univalue subtrees for root)
"""
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return self._unival_subtree(root)[1]
    
    def _unival_subtree(self, root):
        """
        Return is root a univalue subtree, cnt of univalue subtrees for root
        """
        if not root:
            return True, 0
        if not root.left and not root.right:
            return True, 1
        
        is_left, left_cnt = self._unival_subtree(root.left)
        is_right, right_cnt = self._unival_subtree(root.right)
        
        is_root = is_left and is_right and (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val)
        root_cnt = left_cnt + right_cnt + 1 if is_root else left_cnt + right_cnt
        
        return is_root, root_cnt
