Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """invert a binary tree rooted as root, and return its root"""
        if not root:
            return None
        
        # 1. divide 先局部有序
        leftRoot = self.invertTree(root.left)
        rightRoot = self.invertTree(root.right)
        
        # 2. conquer 再整体有序
        root.left = rightRoot
        root.right = leftRoot
        
        return root
     
     
"""
也可以先整体有序，再局部有序
"""
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
               
        return root
