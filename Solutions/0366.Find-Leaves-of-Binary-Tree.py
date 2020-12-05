"""
366. Find Leaves of Binary Tree

Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example:

Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]
 
Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         / 
        2          
 
2. Now removing the leaf [2] would result in this tree:

          1          
 
3. Now removing the leaf [1] would result in the empty tree:

          []         
[[3,5,4],[2],[1]], [[3,4,5],[2],[1]], etc, are also consider correct answers since per each level it doesn't matter the order on which elements are returned.
"""


"""
我们将leaf node的level定义为0, 那么紧紧邻接leaf node的level定义为1；
那么我们只需要将level相同的nodes存在一起就可以了；所以选用dict, key is level, val is a list of nodes on the level.
helper function returns the current level.
"""
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def find_depth(root):
            if not root:
                return 0
            return 1 + max(find_depth(root.left), find_depth(root.right))
            
        def dfs(root):
            """
            return level of the node
            """
            if not root:
                return -1
            
            left_level = dfs(root.left)
            right_level = dfs(root.right)
            
            root_level = 1 + max(left_level, right_level)
            res[root_level].append(root.val)
            
            return root_level
        
        
        depth = find_depth(root)
        res = [[] for _ in range(depth)]
        dfs(root)
        return res
