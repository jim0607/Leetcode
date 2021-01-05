"""
222. Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""


"""
solution 1: dfs to visit every node
"""     
        
"""
solution 2: use the property of complete Tree - O(logN*logN)
Case 1: If left sub tree height equals right sub tree height then:
left subtree is a perfect binary tree, but right subtree may or may not
    1
   / \
  2   3
 / \  /\
4  5 6
Case 2: If left sub tree height greater than right sub tree height then:
# right subtree is a perfect binary tree, but left subTree may or may not

    1
   / \
  2   3
 / \ / \
4   
"""
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_depth = self._depth(root.left)
        right_depth = self._depth(root.right)
        
        if left_depth == right_depth:   # left subtree is a perfect binary tree, but right subtree may or may not
            return 2**left_depth + self.countNodes(root.right)
        elif left_depth > right_depth:  # right subtree is a perfect binary tree, but left subTree may or may not
            return 2**right_depth + self.countNodes(root.left)
        
    def _depth(self, root):     # O(logN)
        if not root:
            return 0
        
        return max(self._depth(root.left), self._depth(root.right)) + 1
    
    
"""
solution 3: similar with Check if value exists in level-order sorted complete binary tree: use gray code to enable binary search in the last level - O(logN* logN)
"""
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        level = self.get_level(root)

        start, end = 0, 2**level - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            gray_code = self.get_graycode(level, mid)
            node = self.get_node_from_graycode(root, gray_code)
            if not node:
                end = mid
            else:
                start = mid
        end_graycode = self.get_graycode(level, end)
        end_node = self.get_node_from_graycode(root, end_graycode)
        if end_node:
            return 2**level - 1 + end + 1
        else:
            return 2**level - 1 + end
        
    def get_level(self, root):
        if not root.left and not root.right:
            return 0
        return 1 + self.get_level(root.left)
    
    def get_graycode(self, level, mid):
        res = []
        for _ in range(level):
            res.append(mid % 2)
            mid //= 2
        return res[::-1]
    
    def get_node_from_graycode(self, root, gray_code):
        for code in gray_code:
            if code == 0:
                root = root.left
            else:
                root = root.right
        return root
