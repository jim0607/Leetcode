Description
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

Example

Example 1:

Input:
     1
   /   \
 -5     2
 / \   /  \
0   2 -4  -5
Output:1


class Solution:
    def findSubtree(self, root):
        if not root:
            return None
            
        self.minSum = float("inf")      # python 这样定义全局变量
        self.minNode = root
        
        self.helper(root)
        
        return self.minNode
        
    # return the subSum with root as its node
    def helper(self, root):
        if not root:
            return 0
            
        # divide
        leftSum = self.helper(root.left)
        rightSum = self.helper(root.right)
        
        # conquer
        subSum = leftSum + rightSum + root.val
        
        if subSum < self.minSum:
            self.minSum = subSum
            self.minNode = root
            
        return subSum
