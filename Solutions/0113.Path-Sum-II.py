Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]


"""碰到打印所有路径的问题，第一反应就是带backtracking the dfs"""
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return
        
        res = []
        self.dfs(root, sum, [], res)
        
        return res
    
    def dfs(self, root, sum, curr, res):
        if not root:
            return
        
        curr.append(root.val)
        
        if not root.left and not root.right:
            if root.val == sum:
                res.append(curr.copy())     # copy takes O(N)

        self.dfs(root.left, sum - root.val, curr, res)  # dfs takes O(N) cuz need to traverse every node
        self.dfs(root.right, sum- root.val, curr, res)
        
        curr.pop()      # backtracking
