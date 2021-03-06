230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 
Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

 

Constraints:

The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.



"""
solution 2: in order traversal of BST (iteratively) - O(k+H) where H is height of tree.
要闭着眼睛都会默写in order traversal的interative版本
"""
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        curr = root
        st = []
        while curr or len(st) > 0:
            while curr:
                st.append(curr)
                curr = curr.left
                
            curr = st.pop()
            
            k -= 1
            if k == 0:
                return curr.val
            
            curr = curr.right

"""
iterative version
"""
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.kthsmallest = root.val
        self._inorder(root)
        return self.kthsmallest
    
    def _inorder(self, root):
        if root.left:
            self._inorder(root.left)
            
        self.k -= 1
        if self.k == 0:
            self.kthsmallest = root.val
            return
        
        if root.right:
            self._inorder(root.right)
            

"""
solution 1: in order traversal of BST - O(N), O(N).
"""
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self._inorder(root)[k-1]
        
    def _inorder(self, root):
        """
        return the in order traversal of the tree
        """
        if not root:
            return []
        
        res = []
        if root.left:
            res += self._inorder(root.left)
        res.append(root.val)
        if root.right:
            res += self._inorder(root.right)
            
        return res
