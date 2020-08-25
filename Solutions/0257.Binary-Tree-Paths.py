Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3


"""
solution 1: dfs
"""
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        def dfs(curr_node, curr_path, res):
            if not curr_node.left and not curr_node.right:
                res.append(curr_path)
                return 
            
            if curr_node.left:
                dfs(curr_node.left, curr_path + "->" + str(curr_node.left.val), res)
            if curr_node.right:
                dfs(curr_node.right, curr_path + "->" + str(curr_node.right.val), res)
                
        res = []
        dfs(root, str(root.val), res)
        
        return res

      
"""
solution 2: divide and conquer
"""
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        """
        return all the binary paths for a tree rooted as root
        """  
        # 3. 递归的出口（结束条件）
        if not root:
            return []
        if not root.left and not root.right:   # 注意这里往往需要判断之后根节点没有左右节点的特殊的情况，养成好习惯，尤其是本题，没有这个判断无法输出正确结果
            return [str(root.val)]
        
        # 1. 递归的拆解之divide：无脑divide 成左右两边
        leftPaths = self.binaryTreePaths(root.left)
        rightPaths = self.binaryTreePaths(root.right)
        
        # 2. 递归的拆解之conquer/merge：这时候要想整棵树在该问题上的结果和左右儿子在该问题上的结果之间的联系是什么，是root.val加上左节点的path，然后root.val加上右节点的path
        rootPaths = []
        for leftPath in leftPaths:
            rootPaths.append(str(root.val) + "->" + leftPath)
        for rightPath in rightPaths:
            rootPaths.append(str(root.val) + "->" + rightPath)
        
        return rootPaths
    
思考：问题有多少个解呢？有多少个Leaf就有多少个解，因为对于每一个leaf，有且仅有一条Path可以到这个leaf
