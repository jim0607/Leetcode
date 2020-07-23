1145. Binary Tree Coloring Game

Two players play a turn based game on a binary tree.  We are given the root of this binary tree, and the number of nodes n in the tree.  n is odd, and each node has a distinct value from 1 to n.

Initially, the first player names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n and y != x.  The first player colors the node with value x red, and the second player colors the node with value y blue.

Then, the players take turns starting with the first player.  In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an uncolored neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)

If (and only if) a player cannot choose such a node in this way, they must pass their turn.  If both players pass their turn, the game ends, and the winner is the player that colored more nodes.

You are the second player.  If it is possible to choose such a y to ensure you win the game, return true.  If it is not possible, return false.

 

Example 1:


Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
Output: true
Explanation: The second player can choose the node with value 2.



"""
check the 3 nodes that are adjacent to node x,
find the number of nodes each subtree has.
If there exist one subtree that has more nodes than other two subtrees add together,
then the second player can color that node.
"""
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, num_x: int) -> bool:
        x = self._locate_node(root, num_x)
        left_nodes = self._find_nodes(x.left)
        right_nodes = self._find_nodes(x.right)
        parent_nodes = self._find_nodes(root) - left_nodes - right_nodes - 1
        
        if left_nodes > (right_nodes + parent_nodes) or \
        right_nodes > (left_nodes + parent_nodes) or \
        parent_nodes > (left_nodes + right_nodes):
            return True
        return False
    
    def _find_nodes(self, root):
        if not root:
            return 0
        
        return 1 + self._find_nodes(root.left) + self._find_nodes(root.right)
    
    def _locate_node(self, root, num_x):
        if not root:
            return None
        
        if root.val == num_x:
            return root
        
        return self._locate_node(root.left, num_x) or self._locate_node(root.right, num_x)
