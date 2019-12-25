Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursion, divide and conquer
# 1. 递归的定义，返回二叉树根节点的路径
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        # divide and conquer不需要helper函数，所以程序的最开始需要定义需要返回的结果
        paths = []
        
        # 3. 递归的出口（结束条件），一般最后写。
        if not root:
            return paths
        if not root.left and not root.right:  # 注意这里往往需要判断之后根节点没有左右节点的特殊的情况，养成好习惯
            return [str(root.val)]
        
        # 2. 递归的拆解之divide：无脑divide 成左右两边
        leftPaths = self.binaryTreePaths(root.left)
        rightPaths = self.binaryTreePaths(root.right)
        
        # 2. 递归的拆解之conquer/merge：这时候要想整棵树在该问题上的结果和左右儿子在该问题上的结果之间的联系是什么，是root.val加上左节点的path，然后root.val加上右节点的path
        for leftPath in leftPaths:
            paths.append(str(root.val) + "->" + leftPath)
        for rightPath in rightPaths:
            paths.append(str(root.val) + "->" + rightPath)
        
        return paths
