337. House Robber III
Medium

2338

49

Add to List

Share
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
    lens = 0
    def rob(self, root: TreeNode) -> int:
        """
        return the max sum of elements withoug connecting each other, for the tree rooted as root
        """
        return max(self.with_without_rob(root)[0], self.with_without_rob(root)[1])
    
    def with_without_rob(self, root):
        """
        return a tuple, the 1st element in the tuple is the max profift with_rob_root
        the 2nd element in the tuple is the max profit without_rob_root
        """
        if not root:
            return (0, 0)
        if not root.left and not root.right:
            return (root.val, 0)
        
        # divide
        with_rob_left, without_rob_left = self.with_without_rob(root.left)
        with_rob_right, without_rob_right = self.with_without_rob(root.right)
        
        # conque
        with_rob_root = root.val + without_rob_left + without_rob_right
        without_rob_root = max(with_rob_left, without_rob_left) + max(with_rob_right, without_rob_right)
        
        return with_rob_root, without_rob_root
