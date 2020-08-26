1110. Delete Nodes And Return Forest

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

 

Example 1:



Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.



"""
we update res as we traverse the tree. we append a node into res if two conditions are satisfied:
1. the node should not be deleted; 2. the node has not parent (meaning it's the root of a forest).
In order to check if a node has parent or not, we need to pass has_parent bool into dfs arguments.
if a node is in to_delete list, then the node should pass the information to it's children that it has been
deleted and it's children has no parent now.
"""
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def helper(root, has_parent):
            """
            Return root
            """
            if not root:
                return None
            
            if root.val in to_delete:
                root.left = helper(root.left, False)
                root.right = helper(root.right, False)
                return None
            else:
                if not has_parent:    # if a node has no parent, then it is a root for a seperate forest
                    res.append(root)
                root.left = helper(root.left, True)
                root.right = helper(root.right, True)
                return root
            
            
        to_delete = set(to_delete)
        res = []
        helper(root, False)

        return res
