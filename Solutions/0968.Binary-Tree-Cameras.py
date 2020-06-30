968. Binary Tree Cameras

Given a binary tree, we install cameras on the nodes of the tree. 

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.


Example 1:

Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:

Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.



"""
solution 1: dp. bottom up:
state0[i] = the min cameras needed to get all the children of node i covered but node i not covered;
state1[i] = the min cameras needed to get all the children of node i and node i covered - no camera on node i;
state2[i] = the min cameras needed to get all the children of node i and node i covered - camera on node i;
"""
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0, 0, 1
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            state0 = left[1] + right[1]
            state1 = min(left[2] + min(right[1:]), right[2] + min(left[1:]))
            state2 = 1 + min(left) + min(right)
            
            return state0, state1, state2
        
        return min(dfs(root)[1:])



"""
Solution 2: Greedy algorithm: 
If a node has children that are not covered by a camera, then we must place a camera here. 
Additionally, if a node has no parent and it is not covered, 因为我们是从下往上的，所以如果this node is not covered, 
then it means it is not covered by it's children, then we must place a camera here.
"""
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        covered = {None}        # 注意初始值是None才是对的，因为后面要判断root.left not in covered
        self.res = 0
        
        def dfs(root, parent):
            if root:
                dfs(root.left, root)
                dfs(root.right, root)
                
                if (parent is None and root not in covered) or root.left not in covered or root.right not in covered:
                    self.res += 1
                    covered.add(parent)
                    covered.add(root)
                    covered.add(root.left)
                    covered.add(root.right)
                    
        dfs(root, None)
        
        return self.res
