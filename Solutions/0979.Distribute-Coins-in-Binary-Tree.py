979. Distribute Coins in Binary Tree

Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

 

Example 1:



Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:



Input: [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.
Example 3:



Input: [1,0,2]
Output: 2
Example 4:



Input: [1,0,0,null,3]
Output: 4


"""
The algorithm is: one node by another, try to balance node from down to top.
helper function returns how many coins should the node receive from it's parent in order to balance itself.
用一个全局变量打擂台记录移动了多少个coins
Time Complexity: O(N), where N is the number of nodes in the tree.
Space Complexity: O(H), where H is the height of the tree.
"""
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.res = 0
        
        def helper(root):
            if not root:
                return 0
            # if not root.left and not root.right:      # 因为后面需要更新self.res, 所以在这里return可能会造成self.res没有更新到
            #     return 1 - root.val
            
            left_should_receive = helper(root.left)       # number of coins the left node should receive from root to make itself balanced
            right_should_receive = helper(root.right)     # number of coins the right node should receive from root to make itself balanced
            
            # self.res += the number of coins moves between root-left, and root-right to make root balanced
            self.res += abs(left_should_receive) + abs(right_should_receive)      
            
            # after giving left_should_receive coins to left and right_should_receive coins to right
            return 1 - root.val + left_should_receive + right_should_receive
        
        helper(root)
        
        return self.res
