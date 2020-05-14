You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        res = 0
        res += self.helper(root, sum)
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        
        return res
    
    # return the cnt for path starting from root that sums up to target
    def helper(self, root, sum):
        if not root:
            return 0
        
        cnt = 0
        if root.val == sum:
            cnt += 1
        
        cnt += self.helper(root.left, sum - root.val)
        cnt += self.helper(root.right, sum - root.val)     
        
        return cnt




Why this solution does not work?

def pathSum(self, root: TreeNode, sum: int) -> int:
    if not root:
        return 0
    
    if not root.left and not root.right:
        if root.val == sum:
            return 1
        else:
            return 0
    
    leftCnt_withoutRoot = self.pathSum(root.left, sum)
    rightCnt_withoutRoot = self.pathSum(root.right, sum)
    
    leftCnt_withRoot = self.pathSum(root.left, sum - root.val)
    rightCnt_withRoot = self.pathSum(root.right, sum - root.val)
    
    return leftCnt_withoutRoot + rightCnt_withoutRoot + leftCnt_withRoot + rightCnt_withRoot
