Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5


"""we can always choose the left middle number as root, or always choose right middle number as root, or sometimes left sometimes right as root. That is why the answer is not unique"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """return the TreeNode converted from nums"""
        if not nums:
            return
        
        lens = len(nums)
        if lens == 1:
            return TreeNode(nums[0])
        
        mid = lens // 2
        root = TreeNode(nums[mid])
        
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return root
