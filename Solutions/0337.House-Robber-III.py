"""
337. House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
"""



"""
    Input: [3,4,5,1,3,null,1]
 input tree            with_without_rob:
     3                  [3+3+1,4+5]
    / \                /        \
   4   5            [4,3]      [5,1]
  / \   \          /     \          \
 1   2   1      [1,0]    [2,0]     [1,0]
                / \       /  \        /  \
           [0,0] [0,0] [0,0] [0,0]  [0,0] [0,0]
"""

class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(root):
            """
            Return the max_sum with_root, without_root
            """
            if not root:
                return 0, 0
            
            # divide
            left_w, left_wo = helper(root.left)
            right_w, right_wo = helper(root.right)
            
            # conquer
            root_w = left_wo + right_wo + root.val
            root_wo = max(left_w, left_wo) + max(right_w, right_wo)
            
            return root_w, root_wo
        
        
        return max(helper(root))
