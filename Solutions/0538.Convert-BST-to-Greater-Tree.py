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
由于visit某一个节点的时候需要用到右边的节点,所以可以做reveerse_order traversal. 
这题跟上面两题有一个相同的特征就是论keep a prev node有多方便
"""
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        self.prev = None      # 论keep a prev node有多方便
        return self._reverse_order(root)
    
    def _reverse_order(self, root):
        if not root:
            return None
        
        self._reverse_order(root.right)
        
        if self.prev:
            root.val += self.prev.val
        self.prev = root    # 论keep a prev node有多方便
        
        self._reverse_order(root.left)
        
        return root
