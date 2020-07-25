1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

Example 1:

Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.



class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_sum = root.val
        q = collections.deque()
        q.append(root)
        level = 0
        res = 1
        while q:
            level += 1
            lens = len(q)
            temp_sum = 0
            for _ in range(lens):
                curr_node = q.popleft()
                temp_sum += curr_node.val
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
                    
            if temp_sum > max_sum:
                max_sum = temp_sum
                res = level
                
        return res
