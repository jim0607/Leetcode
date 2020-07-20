872. Leaf-Similar Trees

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



"""
in order traversal to find the leaves of the tree and put them into a list
"""
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self._find_leaves(root1) == self._find_leaves(root2)
    
    def _find_leaves(self, root):
        if not root:
            return []
        
        res = []
        res += self._find_leaves(root.left)
        if not root.left and not root.right:
            res.append(root.val)
        res += self._find_leaves(root.right)
        
        return res
    
"""
follow up: 这一题是求最后一层的Leaf nodes, 如果需要求最后两层的leaf nodes呢？如果是求最后k层的呢？
那就需要像366那样用dict存level-nodes pair
"""
