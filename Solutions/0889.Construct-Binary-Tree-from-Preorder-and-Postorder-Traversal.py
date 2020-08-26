889. Construct Binary Tree from Preorder and Postorder Traversal

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]


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
"""
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre or not post:
            return None
    
        post_idxmap = collections.defaultdict(int)  # use a hashmap to store num->idx in post
        for i, num in enumerate(post):
            post_idxmap[num] = i
    
        def helper(pre_left, pre_right, post_left, post_right):
            if pre_left >= pre_right or post_left >= post_right:
                return None
            
            root = TreeNode(pre[pre_left])
            pre_left += 1
            post_right -= 1
            
            if pre_left >= pre_right or post_left >= post_right:
                return root
            idx = post_idxmap[pre[pre_left]]
            lens = idx + 1 - post_left      # 左子树区间长度为
            
            root.left = helper(pre_left, pre_left + lens, post_left, idx+1)
            root.right = helper(pre_left + lens, pre_right, idx+1, post_right)
            
            return root
        
        return helper(0, len(pre), 0, len(post))
