129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.



""" solution 1: similar with 113, backtrack O(N)? how to analyze the time complexity of backtrack"""
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.res = 0
        self.backtrack(root, root.val)
        
        return self.res
    
    def backtrack(self, root, pathSum):
        if not root:
            return
        if not root.left and not root.right:
            self.res += pathSum
            return
        
        for currNode in (root.left, root.right):
            if not currNode:
                continue
            temp = pathSum  # 记录一下一会儿好backtrack回来
            pathSum = 10 * pathSum + currNode.val
            self.backtrack(currNode, pathSum)
            pathSum = temp
            
            
""" solution 2: Morris Preorder Traversal  O(N), O(1)"""
