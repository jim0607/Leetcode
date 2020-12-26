Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6


"""方法二：divide and conquer"""
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        left_root = self.flatten(root.left)
        right_root = self.flatten(root.right)
        
        root.left = None
        root.right = left_root
        
        # 下面这个找出left_tail没想出来
        left_tail = root        
        while left_tail.right:
            left_tail = left_tail.right
            
        left_tail.right = right_root
            
        return root


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        if not root.left:
            root.right = self.flatten(root.right)
            return root
        
        left_root = self.flatten(root.left)
        right_root = self.flatten(root.right)
        
        left_tail = left_root
        while left_tail and left_tail.right:
            left_tail = left_tail.right
            
        root.left = None
        root.right = left_root
        left_tail.right = right_root
        
        return root
        
            

"""If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal."""
class Solution:
    # the last node we traversed
    lastNode = None
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        # pre-order 1. node
        if self.lastNode:
            self.lastNode.left = None
            self.lastNode.right = root
        # update last node
        self.lastNode = root
        # in case the flatten(root.left) operation will change root.right, we use a temp to store root.right
        right = root.right      
        # pre-order 2. left
        self.flatten(root.left)
          
        # pre-order 3. right
        self.flatten(right)
        
