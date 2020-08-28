510. Inorder Successor in BST II

Given a node in a binary search tree, find the in-order successor of that node in the BST.

If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
 

Follow up:

Could you solve it without looking up any of the node's values?


"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            right_node = node.right
            while right_node.left:
                right_node = right_node.left
            return right_node
        else:
            parent_node = node.parent
            while parent_node and parent_node.right == node:
                node = parent_node
                parent_node = parent_node.parent
            return parent_node
