"""
404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


"""
dfs to traverse the tree, 当我们遇到leaf节点的时候，我们需要判断其是不是上一个节点的left节点，如果是就更新cnt.
为了判断是不是上一个节点的left节点，我们需要把上一个节点prev_node传到dfs函数arguments中，
这种将prev_node传到dfs中的思想非常重要！
"""
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def helper(root, prev_node):
            if not root:
                return 0
            if not root.left and not root.right and prev_node and root == prev_node.left:
                return root.val

            cnt = 0
            cnt += helper(root.left, root)
            cnt += helper(root.right, root)

            return cnt
        
        return helper(root, None)

    
"""
dfs 中把is_left传入即可
"""
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(root, is_left):
            """
            dfs the tree and return the sum of left leaves
            """
            if not root:
                return 0
            if not root.left and not root.right and is_left:    # if it's a leaf and is_left node
                return root.val

            sums = 0
            if root.left:
                sums += dfs(root.left, True)
            if root.right:
                sums += dfs(root.right, False)
                
            return sums


        return dfs(root, False)
