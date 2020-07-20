530. Minimum Absolute Difference in BST

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).



"""
just in order traversal to turn the tree into a list, and then compare the adjacent elements in a list.
"""
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        in_order = self._in_order(root)
        min_diff = float("inf")
        for i in range(1, len(in_order)):
            min_diff = min(min_diff, abs(in_order[i] - in_order[i-1]))
        return min_diff
    
    def _in_order(self, root):
        if not root:
            return []
        
        res = []
        res += self._in_order(root.left)
        res.append(root.val)
        res += self._in_order(root.right)
        
        return res
