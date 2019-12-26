Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 是BST的话必须满足max of left < root < min of right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root, -float("inf"), float("inf"))[0]
        
    # 1. 递归的定义：返回root为根的树(是不是BST，max and min value in the tree)
    def helper(self, root, maxVal, minVal):
        # 2. 递归的出口：
        if not root:
            return True, -float("inf"), float("inf")
        if not root.left and not root.right:
            return True, root.val, root.val
        
        # 3. 递归的拆解：divide
        isLeftBST, maxLeft, minLeft = self.helper(root.left, maxVal, minVal)
        isRightBST, maxRight, minRight = self.helper(root.right, maxVal, minVal)
        
        # 3. 递归的拆解：conquer （找到拆成左子树之后左右的性质对root这个根节点是什么关系即可）
        if isLeftBST and isRightBST and maxLeft < root.val < minRight:
            return True, max(maxLeft, maxRight, root.val), min(minLeft, minRight, root.val)  # 最开始写找半天错误，最后发现是忘了把root.val加入比较了，本质是忘了递归的定义：返回root为根的树(是不是BST，max and min value in the tree)，想想bottom up的时候这一层算出来的max是要被上面的一层拿出来用的。
        
        return False, -1, -1

Time complexity : O(N) since we visit each node exactly once.
Space complexity : O(N) since we keep up to the entire tree.
