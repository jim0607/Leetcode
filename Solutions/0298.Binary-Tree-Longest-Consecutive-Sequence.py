"""
298. Binary Tree Longest Consecutive Sequence

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
"""




"""
helper function returns (the LCS ended with root, without root)
"""
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        return max(self._helper(root))
    
    def _helper(self, root):
        """
        returns (the LCS ended with root, without root)
        """
        if not root:
            return 0, 0
        if not root.left and not root.right:
            return 1, 0
        
        # divide
        left_w, left_wo = self._helper(root.left)
        right_w, right_wo = self._helper(root.right)
        
        # conquer
        root_wo = max(left_w, left_wo, right_w, right_wo)
        root_w = 1
        if root.left and root.left.val == root.val + 1:
            root_w = max(root_w, 1 + left_w)
        if root.right and root.right.val == root.val + 1:
            root_w = max(root_w, 1 + right_w)
            
        return root_w, root_wo








"""
solution 1: dfs + backtracking using recurssion
"""
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.res = 1
        self.backtracking(root, 1)
        return self.res
    
    def backtracking(self, root, curr):
        if not root:
            return 
        
        self.res = max(self.res, curr)
            
        for node in (root.left, root.right):
            if not node:
                continue
                
            if node.val == root.val + 1:
                curr += 1
                self.backtracking(node, curr)
                curr -= 1
                
            else:   # 如果断掉了，就重新开始搜
                self.backtracking(node, 1)
                  
                  
                  
"""
Solution 2: interative way to implement dfs + backtrack
"""        
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [(root, 1)]
        res = 1
        while stack:
            root, curr = stack.pop()
            res = max(res, curr)
            
            for node in (root.left, root.right):
                if not node:
                    continue
                    
                if node.val == root.val + 1:
                    stack.append((node, curr + 1))
                else:
                    stack.append((node, 1))
                    
        return res


"""
soluiton 3: divide and conquer
"""
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.res = 1
        self.helper(root)
        
        return self.res
        
    def helper(self, root):
        """
        return the Longest Consecutive Sequence started with root node
        """
        if not root:
            return 0

        leftLCS = self.helper(root.left)
        rightLCS = self.helper(root.right)

        rootLCS = 1
        if root.left and root.left.val == root.val + 1:
            rootLCS = max(rootLCS, leftLCS + 1)
        if root.right and root.right.val == root.val + 1:
            rootLCS = max(rootLCS, rightLCS + 1)

        self.res = max(self.res, rootLCS)

        return rootLCS
