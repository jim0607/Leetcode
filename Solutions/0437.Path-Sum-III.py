"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""


"""
solution: dfs every node in the tree. at each node, do a backtrack to find how many root-to-any_node paths are there.
"""
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        res = 0
        res += self._backtrack(root, sum - root.val)
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        
        return res
    
    def _backtrack(self, root, curr_sum):
        """
        return the how many root-to-any_node paths are there 
        """
        cnt = 0
        if curr_sum == 0:   # 从root起点出发，在任意节点都可以停 
            cnt += 1        # 注意这里curr_sum = 0之后不能return, 因为沿着curr_sum=0这条路径往下可能还会有合格的路径

        for next_node in (root.left, root.right):
            if not next_node:
                continue
            cnt += self._backtrack(next_node, curr_sum - next_node.val)
            
        return cnt

"""
how many sub-path that can sum up to k.
presum_dict = defaultdict(int)      presum --> how many times this presum appeared.
curr_pathsum = 从root_node到curr_node前面的那个node(其实是curr_node的parent_node)的path_sum. 
注意curr_pathsum并不包括curr_node在内，这一点与上一题中的presum的定义是一致的。

here subpath_sum = pathsum_from_root_to_curr_node - pathsum_from_root_to_prev_node.
这就相当于arr中的prefix_sum是从arr[0]开始的.
so checking subpath_sum == pathsum_from_root_to_curr_node - pathsum_from_root_to_prev_node
is checking pathsum_from_root_to_curr_node - subpath_sum == pathsum_from_root_to_prev_node ? 
"""
class Solution:
    def pathSum(self, root: TreeNode, k: int) -> int:
        def backtrack(curr_node, curr_pathsum):
            res = 0
            if curr_pathsum - k in pathsum_dict:    # curr_pathsum = 从root_node到curr_node前面的那个node(其实是curr_node的parent_node)的path_sum. 
                res += pathsum_dict[curr_pathsum - k]
                
            for next_node in (curr_node.left, curr_node.right):
                if next_node:
                    pathsum_dict[curr_pathsum] += 1      # 如果选择走curr_node.left或者curr_node.right, 那么肯定要经过curr_node, 所以这条路上的pathsum必须加上curr_pathsum
                    res += backtrack(next_node, curr_pathsum + next_node.val)
                    pathsum_dict[curr_pathsum] -= 1      # backtrack - 如果不选择走curr_node.left或者curr_node.right, 那么肯定不经过curr_node
                    
            return res
        
        if not root:
            return 0
        
        pathsum_dict = defaultdict(int)     # pathsum_from_root_to_curr_node --> how many times this pathsum appeared in the path from root to curr_node
        pathsum_dict[0] = 1
        return backtrack(root, root.val)



Why this solution does not work?

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        if not root:
            return 0
        
        def helper(root, target):
            """
            return how many path sum up to target with/wo starting with root
            """
            if not root:
                return 0, 0
            if not root.left and not root.right:
                if target == root.val:
                    return 1, 0
                return 0, 0
            
            left_w_1, left_wo_1 = helper(root.left, target - root.val)
            left_w_2, left_wo_2 = helper(root.left, target)
            right_w_1, right_wo_1 = helper(root.right, target - root.val)
            right_w_2, right_wo_2 = helper(root.right, target)
            
            root_w = left_w_1 + right_w_1
            root_wo = left_w_2 + left_wo_2 + right_w_2 + right_wo_2
            
            return root_w, root_wo
        
        root_w, root_wo = helper(root, target)
        return root_w + root_wo
