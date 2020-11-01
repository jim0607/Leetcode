"""
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
"""



"""
套用backtrack的模板即可
"""
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return []
        
        def backtrack(curr_node, curr_sum, curr_comb):
            if not curr_node.left and not curr_node.right and curr_sum == target:
                res.append(curr_comb.copy())
                return
            for next_node in (curr_node.left, curr_node.right):
                if next_node:
                    curr_comb.append(next_node.val)
                    backtrack(next_node, curr_sum + next_node.val, curr_comb)
                    curr_comb.pop()
                   
        res = []
        backtrack(root, root.val, [root.val])
        return res





"""碰到打印所有路径的问题，第一反应就是带backtracking the dfs"""
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        self._backtrack(root, sum - root.val, [root.val], res)
        return res
    
    def _backtrack(self, root, curr_sum, curr_path, res):   # dfs takes O(N) cuz need to traverse every node
        if not root.left and not root.right:
            if curr_sum == 0:
                res.append(curr_path.copy())    # # ************ 每次都把.copy忘记了 **********
                return
            
        for next_node in (root.left, root.right):
            if not next_node:
                continue
            curr_path.append(next_node.val)
            # curr_sum += next_node.val， 为什么不在这里对curr_sum做backtrack呢？
            # 因为int是immutable的，所以后面调用backtrack函数是不会改变curr_sum的值的
            # 而curr_path就不一样了，curr_path是一个list, 所以后面调用backtrack函数会改变curr_path的值
            # 这就是为什么我们需要对curr_path做append和pop的操作了
            self._backtrack(next_node, curr_sum - next_node.val, curr_path, res)
            # curr_sum -= next_node.val
            curr_path.pop()
            
 
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
