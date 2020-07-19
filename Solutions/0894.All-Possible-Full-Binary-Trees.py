894. All Possible Full Binary Trees

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

 

Example 1:

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]


class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        def dfs(n):
            if n % 2 != 1:
                return []
            if n in self.memo:
                return self.memo[n]
            
            res = []
            for i in range(1, n, 2):
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(n-1-i):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        res.append(root)
            self.memo[n] = res
            return self.memo[n]
            
        self.memo = collections.defaultdict(list)
        self.memo[1] = [TreeNode(0)]
        return dfs(N)
