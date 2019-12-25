"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        global maxAverage
        maxAverage = -float("inf")
        global maxNode
        self.helper(root)
        return maxAverage

    # 1. 递归的定义：返回以root为根节点subSum和nodeCnt，然后利用这个sum来打擂台比较出maxAverage
    def helper(self, root):
        if not root:
            return 0, 0
        if not root.left and not root.right:
            return root.val, 1
        
        # 2. 递归的拆解之divide：无脑left and right
        leftSubSum, leftNodeCnt = self.helper(root.left)
        rightSubSum, rightNodeCnt = self.helper(root.right)
        
        # 2. 递归的拆解之conquer/merge：
        subSum = leftSubSum + rightSubSum + root.val
        nodeCnt = leftNodeCnt + rightNodeCnt + 1

        # 如果有必要，需要traverse, 也就是打擂台，比较出maxAverage
        global maxAverage
        global maxNode
        if subSum > maxAverage * nodeCnt:       # subSum / nodeCnt > maxAverage 
            maxAverage = subSum / nodeCnt
            maxNode = root
            
        return subSum, nodeCnt
