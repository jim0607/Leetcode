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
            return []
        
        self.res = []
        self.backtrack(root, sum-root.val, [root.val])    # path必须从root出发所以就初始化为sum-root.val, [root.val]
        return self.res
    
    def backtrack(self, root, sum, curr):   # dfs takes O(N) cuz need to traverse every node
        """
        return the path for root that can sum to sum
        """
        if not root.left and not root.right and sum == 0:
            self.res.append(curr.copy())        # ************ 每次都把.copy忘记了 **********
            return
        
        if not root:
            return
        
        for node in (root.left, root.right):
            if not node:
                continue
                
            curr.append(node.val)
            self.backtrack(node, sum - node.val, curr)   
            curr.pop()
            
 
"""
Solution 2: similar with 257 and 112, we just find all the possible paths.
"""
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        def helper(root):
            """
            return all the paths for a tree rooted as root, and their sums
            """
            if not root:
                return [([], float("inf"))]
            
            if not root.left and not root.right:
                return [([root.val], root.val)]
            
            leftPaths = helper(root.left)
            rightPaths = helper(root.right)
            
            rootPaths = []
            for leftPath, leftSum in leftPaths:
                rootPath = [root.val] + leftPath
                rootPaths.append((rootPath, leftSum + root.val))
            for rightPath, rightSum in rightPaths:
                rootPath = [root.val] + rightPath
                rootPaths.append((rootPath, rightSum + root.val))
                
            return rootPaths
        
        res = []
        for path, pathSum in helper(root):
            if pathSum == sum:
                res.append(path)
                
        return res
