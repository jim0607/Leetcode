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


    
    
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        root_not_cv, root_cv_w, root_cv_wo = self._helper(root)
        return min(root_cv_w, root_cv_wo)
    
    def _helper(self, root):
        """
        Return minimum number of cameras needed to cover all the node's children with 
        (node not covered, node covered: 1. with a camera on node, 2. without a camera on node)
        """
        if not root:
            return 0, 1, 0
        
        # 注意left_not_cv, left_cv_w, left_cv_wo经保证root.left的下一层已经cover好了
        # 注意left_not_cv, left_cv_w, left_cv_wo都是从下面一层得到的信息, 与root层无关, 注意left_not_cv表示没有被自己或下一层cover到
        left_not_cv, left_cv_w, left_cv_wo = self._helper(root.left)
        right_not_cv, right_cv_w, right_cv_wo = self._helper(root.right)
        
        # 接下来看看root层, 首先root_not_cv肯定是left has not no camera and right has no camera
        root_not_cv = left_cv_wo + right_cv_wo
        # 然后root covered without a camera肯定是left has a camera or right has a camera, or both have camera
        root_cv_wo = min(left_cv_w + min(right_cv_w, right_cv_wo), right_cv_w + min(left_cv_w, left_cv_wo))
        # 最后root covered with a camera on it肯定是1 + 左边不管有没有被left或left的下一层cover到的最小值 + 右边同样
        root_cv_w = 1 + min(left_not_cv, left_cv_w, left_cv_wo) + min(right_not_cv, right_cv_w, right_cv_wo)
        
        return root_not_cv, root_cv_w, root_cv_wo
    
    
    
    

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
