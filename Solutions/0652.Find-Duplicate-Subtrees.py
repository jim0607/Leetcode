652. Find Duplicate Subtrees

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.



"""
solution: serialize the binary tree using pre-order traversal. O(N^2)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def serialize(root):
            """
            return the serialized str of the tree
            """
            if not root:
                return "None"
            
            left = serialize(root.left)
            right = serialize(root.right)
            
            serialized_str = (str(root.val), left, right)  # O(N), so overall algorithm O(N^2)
            serialized_dict[serialized_str].append(root)
            
            return serialized_str           
        
        # key is str constructed from the root, val is a list of root that can construct into the root
        serialized_dict = collections.defaultdict(list)
        
        serialize(root)
        
        return [serialized_dict[serialized_str][0] for serialized_str in serialized_dict if len(serialized_dict[serialized_str]) >= 2]
        


"""
postOrder traversal with memorization.  still O(N^2)
"""
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        memo = set()
        res = []
        already_added = set()
        
        def postOrder(root):
            """
            return a str constrcucted by a tree
            """
            if not root:
                return "#"
            
            left = postOrder(root.left)
            right = postOrder(root.right)
            
            rootStr = left + right + str(root.val)  # don't know why preOrder and inOrder doesn't work
            
            if rootStr in memo:
                if rootStr not in already_added:
                    already_added.add(rootStr)
                    res.append(root)
            else:
                memo.add(rootStr)
                
            return rootStr

        postOrder(root)
        
        return res
        
        
