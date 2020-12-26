"""
889. Construct Binary Tree from Preorder and Postorder Traversal

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
"""


"""
solution 1: O(N^2).
把这棵树画出来pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1] 自然就明白了代码怎么写了！
"""
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre or not post:
            return None
        
        root = TreeNode(pre.pop(0))
        post.pop()
        
        if not pre: return root
        idx = post.index(pre[0])            
        
        root.left = self.constructFromPrePost(pre[:idx+1], post[:idx+1])
        root.right = self.constructFromPrePost(pre[idx+1:], post[idx+1:])
        
        return root

       
       
       
"""
solution 2: O(N)
1. find the idx for root: pre[start]
2. find the idx for left tree: pre_root_idx + 1
3. find the idx for right tree: post_root_idx - 1
4. recurssive call
"""
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def helper(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None
            if pre_start == pre_end:
                return TreeNode(pre[pre_start])
            
            root = TreeNode(pre[pre_start])
            post_idx = post_idxdict[pre[pre_start+1]]
            pre_idx = pre_idxdict[post[post_end-1]]
            
            root.left = helper(pre_start + 1, pre_idx - 1, post_start, post_idx)
            root.right = helper(pre_idx, pre_end, post_idx + 1, post_end - 1)
            
            return root
        
        pre_idxdict = defaultdict(int)
        for idx, num in enumerate(pre):
            pre_idxdict[num] = idx
        post_idxdict = defaultdict(int)
        for idx, num in enumerate(post):
            post_idxdict[num] = idx
        
        return helper(0, len(pre) - 1, 0, len(post) - 1)
