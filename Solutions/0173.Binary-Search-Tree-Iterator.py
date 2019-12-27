#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#
# https://leetcode.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (52.18%)
# Likes:    1859
# Dislikes: 257
# Total Accepted:    250.4K
# Total Submissions: 480K
# Testcase Example:  '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n[[[7,3,15,null,null,9,20]],[null],[null],[null],[null],[null],[null],[null],[null],[null]]'
#
# Implement an iterator over a binary search tree (BST). Your iterator will be
# initialized with the root node of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# 
# 
# 
# 
# 
# Example:
# 
# 
# 
# 
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false
# 
# 
# 
# 
# Note:
# 
# 
# next() and hasNext() should run in average O(1) time and uses O(h) memory,
# where h is the height of the tree.
# You may assume that next() call will always be valid, that is, there will be
# at least a next smallest number in the BST when next() is called.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# in-order traverse gives an ordered list for BST
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.sortedArr = []
        self.pos = -1
        self._inOrder(root)
    
    def _inOrder(self, root):
        """
        in-order traverse the tree and put items into the sortedArr
        """
        if not root:
            return
        self._inOrder(root.left)
        self.sortedArr.append(root.val)
        self._inOrder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.pos += 1
        return self.sortedArr[self.pos]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.pos + 1 < len(self.sortedArr)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
