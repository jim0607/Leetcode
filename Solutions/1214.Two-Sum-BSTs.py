Given two binary search trees, return True if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.
Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.
Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false

"""solution 2: binary tree traversal using iterative way and store the val in a hash map; time complexity: O(M + N)"""
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if not root1 or not root2:
            return False
        
        stack = []
        numsSet = set()
        
        # in order traversal of a BST using interative way
        curr = root1
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            numsSet.add(curr.val)
            curr = curr.right
            
        # in order traversal of 2nd BST
        curr = root2
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if target - curr.val in numsSet:
                return True
            curr = curr.right
            
        return False

    
    
"""solution 1: recursion (TLE) O(M*N)"""
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if not root1 or not root2:
            return False
        
        if not root1.left and not root1.right and not root2.left and not root2.right:
            return root1.val + root2.val == target

        if target == root1.val + root2.val:
            return True
        
        elif target > root1.val + root2.val:
            return self.twoSumBSTs(root1.right, root2, target) or self.twoSumBSTs(root1, root2.right, target)
        
        else:
            return self.twoSumBSTs(root1.left, root2, target) or self.twoSumBSTs(root1, root2.left, target)
         
