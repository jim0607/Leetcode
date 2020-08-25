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
        
        return self._backtrack(root, root.val)
        
    def _backtrack(self, root, curr_path_sum):
        """
        这里定义_backtrack函数是注意，由于我们想要的res是一个int是immutable的，
        所以不能像113. Path Sum II那样传到backtrack里面去，否则值是传不回来的，
        有两种方法：1. 用一个全局变量self.res; 2. 直接把res return回来
        """
        if not root.left and not root.right:
            return curr_path_sum
        
        res = 0        
        for next_node in (root.left, root.right):
            if not next_node:
                continue
            res += self._backtrack(next_node, curr_path_sum * 10 + next_node.val)
            
        return res


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.res = 0
        self._backtrack(root, root.val)
        return self.res
        
    def _backtrack(self, root, curr_path_sum):
        """
        这里定义_backtrack函数是注意，由于我们想要的res是一个int是immutable的，
        所以不能像113. Path Sum II那样传到backtrack里面去，否则值是传不回来的，
        有两种方法：1. 用一个全局变量self.res; 2. 直接把res return回来
        """
        if not root.left and not root.right:
            self.res += curr_path_sum
            return
      
        for next_node in (root.left, root.right):
            if not next_node:
                continue
            self._backtrack(next_node, curr_path_sum * 10 + next_node.val)
            
""" solution 2: Morris Preorder Traversal  O(N), O(1)"""
