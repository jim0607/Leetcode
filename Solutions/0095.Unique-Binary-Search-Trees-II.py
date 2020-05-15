95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3



class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def helper(start, end):
            """
            return all the path of trees for numbers from start to end
            """
            if start > end:
                return [None, ]
            
            allTrees = []
            for i in range(start, end + 1):
                leftTrees = helper(start, i - 1)
                rightTrees = helper(i + 1, end)
                
                for leftTree in leftTrees:
                    for rightTree in rightTrees:
                        currRoot = TreeNode(i)
                        currRoot.left = leftTree
                        currRoot.right = rightTree
                        allTrees.append(currRoot)
                        
            return allTrees
        
        return helper(1, n)
