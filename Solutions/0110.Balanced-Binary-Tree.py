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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# this is a good example of ResultType in Python. 也就是需要return不止一个值的时候，我们需要将result打包起来。
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root)[0]        
        
    # 1. 递归的定义：返回以root为根的二叉树（是不是balanced, 高度）    
    def helper(self, root: TreeNode) -> (bool, int):
        # 3. 递归的出口：an empty tree is balanced and has a height=-1
        if not root:
            return True, -1
        # 养成好习惯，判断一下
        if not root.left and not root.right:
            return True, 0
        
        # 2. 递归的拆解divide
        leftBalanced, leftHeight = self.helper(root.left)
        rightBalanced, rightHeight = self.helper(root.right)
        
        # 2. 递归的拆解merge
        if not leftBalanced or not rightBalanced or abs(leftHeight - rightHeight) > 1:
            return False, -1
        
        return True, 1 + max(leftHeight, rightHeight)

Time complexity : O(n)
For every subtree, we compute its height in constant time as well as compare the height of its children.
Space complexity : O(n). The recursion stack may go up to O(n) if the tree is unbalanced.
