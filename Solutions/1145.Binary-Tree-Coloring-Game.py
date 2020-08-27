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
The best move y must be immediately adjacent to x, since it locks out that subtree.
check the 3 nodes that are adjacent to node x, find the number of nodes each subtree has.
Then check if palcing ynode at the 3 nodes adjacent to x will end up with more subtree nodes for y.
"""
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        if n == 1:
            return False
        
        xnode = self._findx(root, x)
        
        total_cnt = self._cnt_nodes(root)
        left_cnt = self._cnt_nodes(xnode.left)
        right_cnt = self._cnt_nodes(xnode.right)
        x_cnt = left_cnt + right_cnt + 1
        
        if total_cnt - x_cnt > x_cnt:  # case 1: choose the parent of xnode
            return True
        if left_cnt > total_cnt - left_cnt:          # case 2: choose the left node of xnode as ynode
            return True
        if right_cnt > total_cnt - right_cnt:        # case 3: choose the right node of xnode as ynode
            return True
        
        return False
    
    def _findx(self, root, x):
        if not root:
            return None
        if root.val == x:
            return root
        
        return self._findx(root.left, x) or self._findx(root.right, x)
        
    def _cnt_nodes(self, root):
        if not root:
            return 0
        
        cnt = 1
        cnt += self._cnt_nodes(root.left)
        cnt += self._cnt_nodes(root.right)
        
        return cnt
