1302. Deepest Leaves Sum

Given a binary tree, return the sum of values of its deepest leaves.
 

Example 1:



Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15



"""
first dfs find the max depth, 2nd dfs get the sum of all nodes with max depth.
solution 2: level order bfs, 每次都在while循环里初始化max_depth_sums就可以保证输出的是最后一层的sums了，只需一次遍历
"""
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        max_depth = self._find_max_depth(root, -1)
        self.sums = 0
        self._find_sum(root, 0, max_depth)
        return self.sums
    
    def _find_max_depth(self, root, curr_depth):
        if not root:
            return curr_depth
        
        max_depth = curr_depth
        max_depth = max(max_depth, self._find_max_depth(root.left, curr_depth + 1))
        max_depth = max(max_depth, self._find_max_depth(root.right, curr_depth + 1))
        
        return max_depth
    
    def _find_sum(self, root, curr_depth, max_depth):
        if not root:
            return
        if curr_depth == max_depth:
            self.sums += root.val
            return
        self._find_sum(root.left, curr_depth + 1, max_depth)
        self._find_sum(root.right, curr_depth + 1, max_depth)       
