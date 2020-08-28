897. Increasing Order Search Tree

Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

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
            \
             7
              \
               8
                \
                 9  
 

Constraints:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.


"""
divide and conquer is good - O(N), O(1)
"""
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        left_tree = self.increasingBST(root.left)
        right_tree = self.increasingBST(root.right)
        
        if not left_tree:
            root.left = None        # 注意容易漏掉
            root.right = right_tree
            return root
        
        else:
            curr = left_tree
            while curr.right:
                curr = curr.right
                
            curr.right = root
            root.left = None         # 注意容易漏掉
            root.right = right_tree
            return left_tree



"""
step 1: in order traversal to get a list of node vals;
step 2: construct the tree based on the in_order list
"""
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        in_order = self._in_order(root)
        return self._construct(in_order)
    
    def _in_order(self, root):
        if not root:
            return []
        
        res = []
        if root.left:
            res += self._in_order(root.left)
        res.append(root.val)
        if root.right:
            res += self._in_order(root.right)
            
        return res
            
    def _construct(self, arr):
        if len(arr) == 0:
            return None
    
        root = TreeNode(arr[0])
        root.left = None
        root.right = self._construct(arr[1:])
        
        return root        
