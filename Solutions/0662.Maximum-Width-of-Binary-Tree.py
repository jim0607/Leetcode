"""
662. Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, 
where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
"""



"""
涉及到处理level的信息，就用bfs, q里面存放(node, the postion of the node), 
注意这里的pos到下一层的转换关系: q.append((node.left, 2*pos))
"""
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        max_width = 1
        q = deque()
        q.append((root, 1))         # q里面存放(node, the postion of the node)
        while len(q) > 0:
            lens = len(q)
            for _ in range(lens):
                curr_node, curr_pos = q.popleft()
                if curr_node.left:
                    q.append((curr_node.left, curr_pos * 2))        # 注意这里的pos到下一层的转换关系
                if curr_node.right:
                    q.append((curr_node.right, curr_pos * 2 + 1))
                
            if len(q) > 0:
                max_width = max(max_width, q[-1][1] - q[0][1] + 1)            
            
        return max_width
