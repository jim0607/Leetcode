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
        
        leftHead = self.flatten(root.left)
        rightHead = self.flatten(root.right)
        
        temp = rightHead
        root.right = leftHead
        root.left = None
        
        tail = root
        while tail.right:
            tail = tail.right
            
        tail.right = temp
        
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
        
