Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 方法一：用递归实现 time complexity is O(N)
class Solution:
    # 递归的定义：返回以root为根的二叉树的preorder
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        
        # 递归的出口（结束条件）
        if not root:
            return None
        
        # divide
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        
        # conquer
        result.append(root.val)
        if left:
            result += left  # 注意不要用append. [1,2]+[3,4]=[1,2,3,4], [1,2].append([3,4])=[[1,2], [3,4]]
        if right:
            result += right
        
        return result

      
# this iteration method has to be memorized firmly
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, res = [root], []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return res

# Time complexity : we visit each node exactly once, thus the time complexity is O(N), where N is the number of nodes, i.e. the size of tree.
# Space complexity : depending on the tree structure, we could keep up to the entire tree, therefore, the space complexity is O(N).
