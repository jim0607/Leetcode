"""
1008. Construct Binary Search Tree from Preorder Traversal

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.
"""


"""
solution 1: O(N^2). find the idx of the last node that is less than the root node, 
and use it to construct a left and a right subtree
"""
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        root = TreeNode(preorder.pop(0))
        
        idx = 0
        while idx < len(preorder) and preorder[idx] < root.val:
            idx += 1            # find the first idx that is larger than root.val

        root.left = self.bstFromPreorder(preorder[:idx])
        root.right = self.bstFromPreorder(preorder[idx:])
        
        return root
        

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def build(start, end):
            if start > end:
                return None
            
            root = TreeNode(preorder[start])
            idx = gt[start]
            
            if idx != -1:
                root.left = build(start + 1, idx - 1)
                root.right = build(idx, end)
            else:
                root.left = build(start + 1, end)
                root.right = None
        
            return root        
        
        
        gt = self.find_gt(preorder)
        return build(0, len(preorder) - 1)
    
    
    def find_gt(self, nums):
        """
        use mono stack to find the first idx that is gt than num
        """
        gt = [-1 for _ in range(len(nums))]
        st = []
        for i in range(len(nums) - 1, -1, -1):
            while len(st) > 0 and st[-1][0] < nums[i]:
                st.pop()
            
            if len(st) > 0:
                gt[i] = st[-1][1]
                
            st.append((nums[i], i))
                
        return gt  
        
        
        
        
"""
solution 2: O(N). solution 1 didn't fully take advantage of BST.
we can traverse the preorder list and determine where it can be placed in the subtree.
"""
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            if self.idx >= len(preorder):
                return None
            
            val = preorder[self.idx]
            if val < left or val > right:
                return None
            
            self.idx += 1
            root = TreeNode(val)

            root.left = helper(left, val)
            root.right = helper(val, right)
            
            return root
        
            
        self.idx = 0
        return helper(float("-inf"), float("inf"))
