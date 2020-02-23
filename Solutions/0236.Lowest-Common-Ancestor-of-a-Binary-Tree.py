Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """return the LCA of a tree with root as its root for two nodes p and q"""
        if not root:
            return
        
        if root == p or root == q:
            return root
        
        # divide
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # conquer
        if left and right:  # meaning find p in the left and q in the right
            return root
        elif left:
            return left
        elif right:
            return right
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 方法二：更科学和工程化的做法，用resultType实现divide and conquer (bottom up recursion)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        p_isUnderRoot, q_isUnderRoot, rt = self.helper(root, p, q)
        if p_isUnderRoot and q_isUnderRoot:     # 不要if判断直接return self.helper(root, p, q)[2]也行，这里的if是为了回答follow up questions: what if we do not know whether p, q are nodes in the tree or not.
            return rt
        return None
  
        # 2. 递归的的拆解divide，divide的过程是往下走一步
        p_isInLeft, q_isInLeft, leftNode = self.helper(root.left, p, q)
        p_isInRight, q_isInRight, rightNode = self.helper(root.right, p, q)
        
        p_isUnderRoot = p_isInLeft or p_isInRight or p is root  # bottom up的思想，总有一个点p==root成立，所以不用担心p_isUnderRoot永远为False
        q_isUnderRoot = q_isInLeft or q_isInRight or q is root
        
        # 3. 递归的出口写在这里因为要用到p_isUnderRoot, q_isUnderRoot，只要程序的出口在conquer后面就可以了
        if p is root:
            return True, q_isUnderRoot, root
        if q is root:
            return p_isUnderRoot, True, root
        
        # 2. 递归的拆解conquer，conquer的过程其实是往上走一步，用bottom up的思想去理解会好理解很多
        if leftNode and rightNode:
            return p_isUnderRoot, q_isUnderRoot, root
        if leftNode:
            return p_isUnderRoot, q_isUnderRoot, leftNode
        if rightNode:
            return p_isUnderRoot, q_isUnderRoot, rightNode
        return p_isUnderRoot, q_isUnderRoot, None         
