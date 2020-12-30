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
solution 1: simple recursion - O(N^2), maybe O(nlogn) I think according to Master's theorem.
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder.pop(0))    # this takes O(N), so overall the algorithm takes O(N^2)
        idx = inorder.index(root.val)       # this takes O(N), so overall the algorithm takes O(N^2)
            
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
        
        return root
        
        
        
"""
solution 1中需要O(N^2)的原因是1. preorder.pop(0) takes O(N). We can convert preorder into a q and popleft.
2. finding the idx in inorder list takes O(N). We can use a hash table to store num-to-idx pair in advance.
This leads to solution 2, which takes O(N) instead of O(N^2).
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(preorder_q, start, end):
            if start >= end:
                return None
            
            root = TreeNode(preorder_q.popleft())   # now this takes O(1)
            idx = inorder_idx[root.val]             # now this takes O(1)
            
            # 注意此时必须把start和idx都传进helper function, 因为如果传inorder[:idx]的话，
            # 会导致后面找inorder[:idx]这个subarray中的idx的时候和hash table中的不一样
            root.left = helper(preorder_q, start, idx)  
            root.right = helper(preorder_q, idx + 1, end)
            
            return root
        
        
        preorder_q = collections.deque(preorder)    # use a queue to store preorder list
        inorder_idx = collections.defaultdict(int)  # use a hash table to store num-to-idx pair
        for i, num in enumerate(inorder):
            inorder_idx[num] = i
            
        return helper(preorder_q, 0, len(inorder))
    
    
    
    
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(in_start, in_end):
            if in_start >= in_end:
                return None
            
            root = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1
            in_idx = num_idx[root.val]
            
            root.left = build(in_start, in_idx)
            root.right = build(in_idx + 1, in_end)
            
            return root
        
        
        num_idx = defaultdict(int)
        for idx, num in enumerate(inorder):
            num_idx[num] = idx
        
        self.pre_idx = 0
        return build(0, len(inorder))
