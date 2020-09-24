"""
653. Two Sum IV - Input is a BST

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7
Target = 9
Output: True
"""



"""
iterative in-order traversal of a tree要背熟
"""
class Solution:
    def findTarget(self, root: TreeNode, target: int) -> bool:
        if not root or not root.left and not root.right:
            return False
        
        num_set = set()
        curr = root
        st = []
        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            
            if target - curr.val in num_set:
                return True
            num_set.add(curr.val)
            
            curr = curr.right
        return False



Solution 1: First convert the BST into a sortedArr using inorder traversal, then use two pointer method to do the two sum problem
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        
        sortedArr = self.inorder(root)
        i, j = 0, len(sortedArr) - 1
        while i < j:
            if sortedArr[i] + sortedArr[j] > k:
                j -= 1
            elif sortedArr[i] + sortedArr[j] < k:
                i += 1
            else:
                return True
            
        return False
        
    def inorder(self, root):
        res = []
        if not root:
            return res
        
        if root.left:
            res += self.inorder(root.left)
        res.append(root.val)
        if root.right:
            res += self.inorder(root.right)
            
        return res        
