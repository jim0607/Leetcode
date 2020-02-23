Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum average.

Have you met this question in a real interview?  
Example
Example 1

Input：
{1,-5,11,1,2,4,-2}
Output：11
Explanation:
The tree is look like this:
     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2 
The average of subtree of 11 is 4.3333, is the maximun.


class Solution:
    def findSubtree2(self, root):
        if not root:
            return
        
        self.maxAvg = -float("inf")
        self.maxAvgNode = None
        
        self.helper(root, 0)
        
        return self.maxAvgNode
        
    def helper(self, root, nodeNum):
        # return the subSum of the tree root as its root, and also return the nodeNum
        if not root:
            return 0, 0
            
        # divide
        leftSum, leftNum = self.helper(root.left, nodeNum)
        rightSum, rightNum = self.helper(root.right, nodeNum)
        
        # conquer
        subSum = leftSum + rightSum + root.val
        subNodeNum = leftNum + rightNum + 1
        
        # traverse to conpare, 打擂台
        subAvg = subSum / subNodeNum
        if subAvg > self.maxAvg:
            self.maxAvg = subAvg
            self.maxAvgNode = root
            
        return subSum, subNodeNum
