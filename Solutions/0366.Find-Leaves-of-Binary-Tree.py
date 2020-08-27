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
我们将leaf node的level定义为0, 那么紧紧邻接leaf node的level定义为1；
那么我们只需要将level相同的nodes存在一起就可以了；所以选用dict, key is level, val is a list of nodes on the level.
helper function returns the current level.
"""
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        def helper(root):
            if not root:
                return 0
            
            left_level = helper(root.left)
            right_level = helper(root.right)
            
            root_level = max(left_level, right_level) + 1
            levels[root_level].append(root.val)
            
            return root_level
        
        levels = collections.defaultdict(list)  # key is level, val is a list of nodes on the level
        helper(root)
        
        res = []
        for level in sorted(levels):
            res.append(levels[level])
        return res
