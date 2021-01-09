"""
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
"""



class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(start, end):
            """
            return all the path of trees for numbers from start to end
            """
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]
            
            res = []
            for mid in range(start, end + 1):
                left_trees = helper(start, mid - 1)
                right_trees = helper(mid + 1, end)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(mid)    # 注意这个不能写到两个for loop 外面去了的！！！不然root的连接关系就不对了
                        root.left = left
                        root.right = right
                        res.append(root)
            return res
            
        if n == 0:
            return []
        return helper(1, n)
