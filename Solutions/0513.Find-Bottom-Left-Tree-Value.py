513. Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        bottom_left = root.val
        q = collections.deque()
        q.append(root)
        while len(q) > 0:
            curr_node = q.popleft()
            bottom_left = curr_node.val
            if curr_node.right:         # right first, then left
                q.append(curr_node.right)
            if curr_node.left:
                q.append(curr_node.left)
        return bottom_left
