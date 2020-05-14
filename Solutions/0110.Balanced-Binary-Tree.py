Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.is_balanced = True    # 定义一个全局变量
        
        self.helper(root)
        
        return self.is_balanced
    
    def helper(self, root):
        """递归的定义: return the depth of the tree with root as its root"""
        # 1. 初始条件
        if not root:
            return 0
        # 2. 初始条件，养成好习惯，把叶子节点单独做判断
        if not root.left and not root.right:
            return 1
        
        # 3. 递归的拆解：divide
        leftDepth = self.helper(root.left)
        rightDepth = self.helper(root.right)
        
        # 4. 递归的拆解：merge
        if abs(leftDepth - rightDepth) > 1:
            self.is_balanced = False
            
        return max(leftDepth, rightDepth) + 1

# this is a good example of ResultType in Python. 也就是需要return不止一个值的时候，我们需要将result打包起来。
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def helper(root):
            """
            return (if the tree is balanced, maxDepth)
            """
            if not root:
                return (True, 0)
            
            leftIsBalan, leftMaxDepth = helper(root.left)
            rightIsBalan, rightMaxDepth = helper(root.right)
            
            rootIsBalan = leftIsBalan and rightIsBalan and abs(leftMaxDepth - rightMaxDepth) <= 1
            rootMaxDepth = max(leftMaxDepth, rightMaxDepth) + 1
            
            return (rootIsBalan, rootMaxDepth)
        
        return helper(root)[0]
       
       
Time complexity : O(n)
For every subtree, we compute its height in constant time as well as compare the height of its children.
Space complexity : O(n). The recursion stack may go up to O(n) if the tree is unbalanced.
