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
        
        def dfs(curr_node, curr_sum):
            if not curr_node:
                return 0
            res = pre_sum[curr_sum - target]
            pre_sum[curr_sum] += 1
            if curr_node.left: res += dfs(curr_node.left, curr_sum + curr_node.left.val)
            if curr_node.right: res += dfs(curr_node.right, curr_sum + curr_node.right.val)
            pre_sum[curr_sum] -= 1      # 做backtrack
            return res
        
        
        pre_sum = collections.defaultdict(int)  # presum --> how many paths have this presum accured
        pre_sum[0] = 1
        return dfs(root, root.val)




Why this solution does not work?

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        cnt = 0
        if sum == 0:
            cnt += 1

        cnt += self.pathSum(root.left, sum)             # left cnt without root
        cnt += self.pathSum(root.right, sum)            # right cnt without root

        cnt += self.pathSum(root.left, sum - root.val)  # left cnt with root
        cnt += self.pathSum(root.right, sum - root.val) # riight cnt with root

        return cnt
