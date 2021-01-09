"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


   
"""
solution 1: similar with 95 - O(Catalan number)
"""
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        def helper(start, end):
            """
            return all the possible paths from start to end
            """
            if start > end:
                return [None]
            
            alltrees = []
            for i in range(start, end + 1):
                left_trees = helper(start, i-1)
                right_trees = helper(i+1, end)
                for left in left_trees:
                    for right in right_trees:
                        curr_root = TreeNode(i)
                        curr_root.left = left
                        curr_root.right = right
                        alltrees.append(curr_root)
                        
            return alltrees
        
        return len(helper(1, n))
   
   
"""
solution 2: DP
If we examine the above brutal force solution carefully, there are two loops for left and right trees.
Actually, we only need to know how many number of trees in the left say l, and how many in the right say r.
Then the total number of possible tree paths is l * r.
If we defind dp[i] = how many trees possible in a range with width == i, then we have
dp[j] = sum for (dp[i] * dp[j - i - 1] for all i < j)
O(N^2)
"""
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1    # None is also a considered a subtree
        dp[1] = 1
        
        for j in range(2, n + 1):
            for i in range(j):
                dp[j] += dp[i] * dp[j - i - 1]
                
        return dp[-1]
   
   

   
"""dolution 3: math
卡塔兰数 Catalan Number 的一个例子
https://www.cnblogs.com/grandyang/p/4299608.html"""
class Solution:
    def numTrees(self, n: int) -> int:
        C = 1
        for i in range(n):
            C = C * (2 * (2 * i + 1) / (i + 2))
            
        return int(C)
