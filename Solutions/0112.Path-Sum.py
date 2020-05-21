Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


"""
Solution 1: similar with 257, find all the paths and put all the pathSums in a set. 
"""
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        def helper(root):
            """
            return a set of all the possible sums in the tree rooted as root
            """
            if not root:
                return {float("inf")}       # 注意这里不要返回{0}, 因为我们的sum的终点必须是叶子节点，而不是None节点，想想一个[1,2], sum=1的例子，我们不能返回True因为右节点不是叶子节点而是None
            if not root.left and not root.right:
                return {root.val}

            leftPathSums = helper(root.left)
            rightPathSums = helper(root.right)
        
            rootPathSums = set()
            for leftPathSum in leftPathSums:
                rootPathSums.add(leftPathSum + root.val)
            for rightPathSum in rightPathSums:
                rootPathSums.add(rightPathSum + root.val)
                
            return rootPathSums
        
        return sum in helper(root)


"""
Solution 2: I would say this is good ans smart! This is just normal DFS.
"""
class Solution:
    # the function returns whether of not starting from root, there is a path sums to target
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == sum
        
        leftHas = self.hasPathSum(root.left, sum - root.val)
        rightHas = self.hasPathSum(root.right, sum - root.val)
        
        return leftHas or rightHas
