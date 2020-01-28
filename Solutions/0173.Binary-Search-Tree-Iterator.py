173. Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Example:
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.


"""Solution 1: use queue"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.q = collections.deque()
        self.root = root
        
        self._inOrder(self.root)
        
    # in order traversal BST gives a sorted array
    def _inOrder(self, root: TreeNode):
        if not root:
            return
        
        self._inOrder(root.left)    # 题目把None也作为输入了，所以这里不要判断if root.left:
        self.q.append(root.val)
        self._inOrder(root.right)
            
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if not self.hasNext():
            return None
        
        return self.q.popleft()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.q) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

"""Solution 2: use arr and a pointer"""
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
