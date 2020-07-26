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
We pass the minimum and maximum values to the children,
At the leaf node, we return max - min through the path from the root to the leaf.
Since DFS works going finished path by finished path, so values are not corrupted between impossible paths.
这个递归真的需要好好理解
"""
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self._dfs(root, root.val, root.val)
    
    def _dfs(self, root, max_num, min_num):
        if not root:
            return 0
        
        max_num = max(max_num, root.val)
        min_num = min(min_num, root.val)
        
        left_diff = self._dfs(root.left, max_num, min_num)
        right_diff = self._dfs(root.right, max_num, min_num)
        
        return max(left_diff, right_diff, max_num - min_num)
