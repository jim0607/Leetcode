"""
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


"""
solution 1: in order traversal the BST and compare the prev_node and curr_node as we go. 
Need to use a global prev_node while doing in_order traversal. maintain a global prev_node的思想非常重要
"""
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.min_diff = sys.maxsize
        self.prev_num = sys.maxsize
        self.in_order(root)
        return self.min_diff
    
    def in_order(self, curr):
        """
        In order traversal the tree and update min_diff
        """
        if curr.left:
            self.in_order(curr.left)
            
        self.min_diff = min(self.min_diff, abs(curr.val - self.prev_num))
        self.prev_num = curr.val   # 注意in-order traversal prev change to curr
        
        if curr.right:
            self.in_order(curr.right)


"""
solutio 2: in order traversal to turn the tree into a list, and then compare the adjacent elements in a list.
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
