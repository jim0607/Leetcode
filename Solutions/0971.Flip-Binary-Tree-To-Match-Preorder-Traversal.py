971. Flip Binary Tree To Match Preorder Traversal

Given a binary tree with N nodes, each node has a different value from {1, ..., N}.

A node in this binary tree can be flipped by swapping the left child and the right child of that node.

Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values the voyage of the tree.

(Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)

Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.

If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.

If we cannot do so, then return the list [-1].

Example 1:
Input: root = [1,2], voyage = [2,1]
Output: [-1]
Example 2:



Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
Example 3:

Input: root = [1,2,3], voyage = [1,2,3]
Output: []



注意construct the tree using the voyage list的方法行不通因为仅通过一个list是没办法重构一个Tree的

"""
Return whether or not it matches to voyage. as we traverse the tree, use an index to in voyage v.
If current node == null, it's fine, we return true
If current node.val != arr[i], doesn't match wanted value, return false
If node.val != arr[i+1], flip left and right child.
"""
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        def dfs(root):
            """
            Return whether or not it matches to voyage
            """
            if not root:
                return True
            if root.val != voyage[self.idx]:
                return False
            
            self.idx += 1
            if root.left and root.left.val != voyage[self.idx]:
                res.append(root.val)
                root.left, root.right = root.right, root.left
                
            return dfs(root.left) and dfs(root.right)
            
            
        self.idx = 0    # 这里必须用self.idx因为int是immutable的，如果是是List就不需要self了
        res = []        # 这里就不需要self了，因为List is mutable
        match = dfs(root)
        
        return res if match else [-1]
