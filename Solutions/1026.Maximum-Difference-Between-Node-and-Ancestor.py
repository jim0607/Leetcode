"""
1026. Maximum Difference Between Node and Ancestor

Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)


Example 1:

Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
"""

"""
helper function return max, min in root tree.  self.max_diff 打擂台.
"""
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def helper(root):
            """
            return max, min in root tree
            """
            if not root.left and not root.right:
                return root.val, root.val
            
            root_max, root_min = root.val, root.val
            if root.left:
                left_max, left_min = helper(root.left)
                root_max = max(root_max, left_max)
                root_min = min(root_min, left_min)
            if root.right:
                right_max, right_min = helper(root.right)
                root_max = max(root_max, right_max)
                root_min = min(root_min, right_min)
            
            self.max_diff = max(self.max_diff, abs(root.val - root_max), abs(root.val - root_min), abs(root.val - root_min), abs(root.val - root_max))
            
            return root_max, root_min
            
        
        self.max_diff = -sys.maxsize
        helper(root)
        return self.max_diff



"""
solution 1: dfs visit every node, at each node, stop there and find the max and min of its subtree to get its max_diff.
since finding max and min of subtee takes O(N), so the overall time comlexity is O(N^2).
"""
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_max_diff = self.maxAncestorDiff(root.left)
        right_max_diff = self.maxAncestorDiff(root.right)
        
        left_max, left_min = self._find_maxmin(root.left)
        right_max, right_min = self._find_maxmin(root.right)
        
        root_max_diff = 0
        if left_max is not None:   # 最好是乖乖写is not None, 因为left_max可能等于0, 导致两个test case过不了
            root_max_diff = max(root_max_diff, abs(left_max - root.val), abs(left_min - root.val))
        if right_max is not None:
            root_max_diff = max(root_max_diff, abs(right_max - root.val), abs(right_min - root.val))
        
        return max(root_max_diff, left_max_diff, right_max_diff)
    
    
    def _find_maxmin(self, root):
        if not root:
            return None, None
        if not root.left and not root.right:
            return root.val, root.val
        
        left_max, left_min = self._find_maxmin(root.left)
        right_max, right_min = self._find_maxmin(root.right)
        
        root_max, root_min = root.val, root.val
        if left_max is not None:    # 最好是乖乖写is not None, 因为left_max可能等于0, 导致两个test case过不了
            root_max, root_min = max(root_max, left_max), min(root_min, left_min)
        if right_max is not None:
            root_max, root_min = max(root_max, right_max), min(root_min, right_min)

        return root_max, root_min
