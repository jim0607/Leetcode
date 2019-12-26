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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""方法二：divide and conquer"""
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.helper(root)
        
    def helper(self, root: TreeNode) -> "TreeNode":
        """
        return the last node of root
        """
        if not root:
            return
        
        # divide
        left_last = self.helper(root.left)
        right_last = self.helper(root.right)
        
        # conquer
        # connect the left_last with the right_first, which is root.right
        if left_last:
            left_last.right = root.right
            root.right = root.left
            root.left = None
        
        # 这里顺序很重要，一定是先return right_last，再return left_last，都为None的话return root，因为如果把root排好了之后right_last应该是最后一个节点了
        if right_last: 
            return right_last
        
        if left_last:
            return left_last

        return root
