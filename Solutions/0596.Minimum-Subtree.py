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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 注意不能在这里写maxSum = -float("inf")来定义全局变量https://www.cnblogs.com/chaoguo1234/p/9246791.html，python必须每次调用全局变量的时候都要声明是全局变量
    # 由于这里return value不可能是最后的maxSum，因为需要比较，所以要用到traverse
    def maxPathSum(self, root: TreeNode) -> int:
        global minSum   #python必须每次调用全局变量的时候都要声明是全局变量
        minSum = float("inf")
        global minNode
        minNode = root
        self.Helper(root, 0)
        return minNode
        
    # 1. 递归的定义,返回以root为根的所有子树中的subSum    
    def Helper(self, root: TreeNode, subSum: int) -> int:
        # 3. 递归的出口
        if not root:
            return 0
        
        # 2. 递归的拆解：divide and merge
        leftSum = self.Helper(root.left, subSum)  # 无脑写出左右两部分
        rightSum = self.Helper(root.right, subSum)
        subSum = root.val + leftSum + rightSum
                
        # 这里用到了traverse，用打擂台法找到maxSum
        global minSum   # python必须每次调用全局变量的时候都要声明是全局变量
        global minNode
        if subSum < minSum:
            minSum = subSum
            minNode = root
            
        return subSum
