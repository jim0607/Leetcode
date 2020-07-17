105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
   
   
   
"""
solution 1: simple recursion - O(N^2)
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        
        root = TreeNode()
        root.val = preorder.pop(0)  # this takes O(N), so overall the algorithm takes O(N^2)
        
        # find the index where root.val is in inorder list
        # this takes O(N), so overall the algorithm takes O(N^2)
        idx = 0         
        for i, num in enumerate(inorder):
            if num == root.val:
                idx = i
                break
            
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
        
        return root
        
        
        
"""
solution 1中需要O(N^2)的原因是1. preorder.pop(0) takes O(N). We can convert preorder into a deque and popleft.
2. finding the idx in inorder list takes O(N). We can use a hash table to store num-to-idx pair in advance.
This leads to solution 2, which takes O(N) instead of O(N^2).
"""
"""
solution 1中需要O(N^2)的原因是1. preorder.pop(0) takes O(N). We can convert preorder into a deque and popleft.
2. finding the idx in inorder list takes O(N). We can use a hash table to store num-to-idx pair in advance.
This leads to solution 2, which takes O(N) instead of O(N^2).
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        
        preorder_dq = collections.deque(preorder)       # use a deque to store preorder list
        inorder_idxmap = collections.defaultdict(int)   # use a hash table to store num-to-idx pair
        for i, num in enumerate(inorder):
            inorder_idxmap[num] = i
            
            
        def helper(preorder_dq, i, j):     # i, j are idx in inorder list
            if not preorder_dq:
                return None
            
            if i >= j:
                return None
            
            root = TreeNode()
            root.val = preorder_dq.popleft()  # this takes O(1)
        
            # find the index where root.val is in inorder list - O(1)
            idx = inorder_idxmap[root.val]
            
            root.left = helper(preorder_dq, i, idx)
            root.right = helper(preorder_dq, idx + 1, j)
        
            return root
        
        
        return helper(preorder_dq, 0, len(inorder))
