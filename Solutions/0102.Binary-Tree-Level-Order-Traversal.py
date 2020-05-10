#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (51.36%)
# Likes:    2090
# Dislikes: 57
# Total Accepted:    486.7K
# Total Submissions: 945.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#

"""Time complexity : O(N) since each node is processed exactly once.
Space complexity : O(N) to keep the output structure which contains N node values."""

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        # 非常typical的BFS解binary tree的模板
        res = []
        q = deque()
        q.append(root)
        while q:
            level = []
            lens = len(q)  # important, 注意这里定义一个lens而不是在59行里直接用len(q)是因为每次q.popleft()之后q的长度会变！
            # 用一个for循环来处理每一层
            for _ in range(lens):
                # 在这一层要做两件事情：1. 处理这一层：将该层的所有的node.val依次放入level中
                node = q.popleft()
                level.append(node.val)
                # 2. 处理下一层：将该层所有的node的左右子节点依次入队列
                if node.left:  # 注意这里判断是为了不把None放到队列里去，这样res出来的结果就没有None了。
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res

# @lc code=end
