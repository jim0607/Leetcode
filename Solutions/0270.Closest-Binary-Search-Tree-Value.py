270. Closest Binary Search Tree Value

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4



"""
Interative地遍历BST的方法好生疏，但是更直观一些！
- O(h) time where h is the height of the tree
"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(x - target))   # 这写法新奇！
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return closest
        
        
"""
recursion版本
"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.closest = root.val
        self._dfs(root, target)
        return self.closest
        
    def _dfs(self, root, target):
        if not root:
            return

        self.closest = min(root.val, self.closest, key = lambda x: abs(x - target))   # 这写法新奇！
        
        if target < root.val:
            self._dfs(root.left, target)
        else:
            self._dfs(root.right, target)
