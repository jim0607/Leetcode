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


"""
right to left bfs
"""
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return None
        
        q = collections.deque()
        q.append(root)
        while q:
            lens = len(q)
            for _ in range(lens):
                curr = q.popleft()
                if curr.right:      # right first, then left
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
                    
        return curr.val
