Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42


"""这个题目对于path的定义描述的不好，题意应该是任何path都可以，只要点和点连接在一起就算一个path，起点和终点doesn't matter"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = root.val
              
        self.helper(root)
        
        return self.maxSum
    
    def helper(self, root):
        """return the maxPathSum for tree ended with root"""
        if not root:
            return 0
        """ if not root.left and not root.right: # 注意不能加这一句，因为如果加这一句的话还没有打擂台得到self.maxSum就已经return了
            return root.val """  
        # divide
        leftPathSum = max(self.helper(root.left), 0)    # 如果left的最大的possible sum<0那就不加leftPath了，反正起点终点都没限制，任何节点都可加可不加
        rightPathSum = max(self.helper(root.right), 0)
        
        # conquer
        self.maxSum = max(self.maxSum, leftPathSum + rightPathSum + root.val)
        
        return max(leftPathSum, rightPathSum) + root.val
