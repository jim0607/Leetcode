"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.

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
"""


"""
这个题目对于path的定义描述的不好，题意应该是任何path都可以，只要点和点连接在一起就算一个path，起点和终点doesn't matter
用一个self.max_sum去打擂台as we traverse the tree.
"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = root.val
        self.helper(root)
        return self.maxSum
    
    def helper(self, root):
        """
        return the maxPathSum for tree ended with root
        """
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



class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        returns the maxSum for the tree with/wo root in the path
        """
        self.maxSum = -float("inf")
        self.helper(root)
        return self.maxSum
        
    def helper(self, root):
        """
        returns the maxSum for the tree ended with root in the path
        """
        if not root:
            return -float("inf")    # 如果root=none就不加进去
        
        if not root.left and not root.right:    # 也可以不要这一句，但是加上这句会快很多，因为省去了not root return float("inf")之后的比较
            self.maxSum = max(self.maxSum, root.val)    # 注意不要忘了在这里打擂台
            return root.val 
        
        # divide
        leftMaxSum = self.helper(root.left)     # the max ended with root.left
        rightMaxSum = self.helper(root.right)   
        
        # conquer
        # rootMaxSum is defined as the maxSum ended with root
        rootMaxSum = max(leftMaxSum + root.val, rightMaxSum + root.val, root.val)
        rootMaxSum_pass_root = leftMaxSum + rightMaxSum + root.val  # maxSum pass root
        self.maxSum = max(rootMaxSum, rootMaxSum_pass_root, self.maxSum)
        
        return rootMaxSum


"""
O(N^2) - 在binary tree里求longest path问题，如果任何path都算数的话，那么我们在divide and conquer的时候要分成两种情况讨论：
1. path ended with root; 2: path not ended with root. 我们往往需要在helper函数中返回end_w和end_wo两种情况的值, 
有时候也可以将case 2细分为: I. path pass the root, and II. path without the root.
"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return float("-inf")
        
        start_w_root = self._max_path_sum_started_w(root)
        pass_root = root.val + self._max_path_sum_started_w(root.left) + self._max_path_sum_started_w(root.right)
        wo_root = max(self.maxPathSum(root.left), self.maxPathSum(root.right))
        
        return max(start_w_root, pass_root, wo_root)
        
    def _max_path_sum_started_w(self, root):
        """
        Return the max path sum started with root
        """
        if not root:
            return float("-inf")
        
        left = self._max_path_sum_started_w(root.left)
        right = self._max_path_sum_started_w(root.right)
        
        return max(left + root.val, right + root.val, root.val)
