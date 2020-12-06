538. Convert BST to Greater Tree

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/


      
"""
use a global self.pre_sum as we reverse_in_order traversal the tree - recurssively
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def reverse_order(curr_node):
            if curr_node.right:
                reverse_order(curr_node.right)
                
            curr_node.val += self.prev_num
            self.prev_num = curr_node.val
                
            if curr_node.left:
                reverse_order(curr_node.left)
                
                
        self.prev_num = 0
        reverse_order(root)
        return root
      
      
      
      
"""
use a global self.pre_sum as we reverse_in_order traversal the tree - iteratively
"""
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        pre_sum = 0
        st = []
        curr = root
        while curr or len(st) > 0:
            while curr:
                st.append(curr)
                curr = curr.right   # 注意这里是curr = curr.right因为是reversed_in_order
            
            curr = st.pop()
            curr.val += pre_sum
            pre_sum = curr.val
            
            curr = curr.left
        
        return root
