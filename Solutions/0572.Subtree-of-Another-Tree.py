572. Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
 

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.




"""
solution 1: brutal force: dfs to visit every node, at each node, stop and check if the subtree rooted
as that node is the same as t - O(MN)
"""
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        
        left_is_subtree = self.isSubtree(s.left, t)
        right_is_subtree = self.isSubtree(s.right, t)
        
        if left_is_subtree or right_is_subtree or self._helper(s, t):
            return True
        
        return False
    
    def _helper(self, s, t):
        """
        return if the subtree rooted as s is the same as t
        """
        if not s and not t:
            return True
        elif not s:
            return False
        elif not t:
            return False
        elif s.val != t.val:
            return False
        
        left = self._helper(s.left, t.left)
        right = self._helper(s.right, t.right)
        return left and right
        
        
        
"""
solution 2: O(M+N).  we can in order traversal the two trees and turn them into two strings s and t. 
Then the problem becomes exactly the same as finding a substring in s that equals t, which is 28. Implement strStr().
Use rolling hash, we can realize O(M+N) solution.
"""
