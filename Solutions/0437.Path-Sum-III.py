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
solution 2: the above solution is easy to understand, but it takes O(N^2).
presum solution: O(N). Use a presum to record presum --> how many paths have this presum accured
"""
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        if not root:
            return 0
        
        def backtrack(curr_node, curr_sum):
            if not curr_node:
                return 0
            
            res = presum_dict[curr_sum - target]    # 注意curr_sum等价于prefix_sum[j]
            for next_node in (curr_node.left, curr_node.right):
                if next_node:
                    presum_dict[curr_sum] += 1
                    res += backtrack(next_node, curr_sum + next_node.val)
                    presum_dict[curr_sum] -= 1      # 做backtrack
            
            return res
        
        
        presum_dict = defaultdict(int)  # presum --> how many paths have this presum occured
        presum_dict[0] = 1
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
