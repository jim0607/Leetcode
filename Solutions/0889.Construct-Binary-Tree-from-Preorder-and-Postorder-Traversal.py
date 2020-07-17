889. Construct Binary Tree from Preorder and Postorder Traversal

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]



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
