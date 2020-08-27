314. Binary Tree Vertical Order Traversal

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]


"""
solution: record the position of each node as we dfs to traverse the tree 
"""
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
              
            
        def dfs(root, level, pos):
            if not root:
                return
            
            position.append((level, pos, root.val))
            dfs(root.left, level + 1, pos - 1)
            dfs(root.right, level + 1, pos + 1)            
            
            
        position = []
        dfs(root, 0, 0)
        position.sort(key = lambda x: (x[1], x[0]))   
        
        res = []
        i = 0
        while i < len(position):
            pos = position[i][1]
            temp = []
            while i < len(position) and position[i][1] == pos:
                temp.append(position[i][2])
                i += 1
            res.append(temp)
        return res




"""
Previous solution
"""
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        # step 1: 找到树的深度和宽度
        depth = self._find_depth(root, 0)
        leftmost = self._find_leftmost(root)
        rightmost = self._find_rightmost(root)

        # step 2: df每个node并且把node的位置信息存到一个dict中
        res = collections.defaultdict(list)
        self._dfs(root, leftmost, 0, res)
        
        # step 3: sort dictionary得到ans
        ans = []
        for y_pos in sorted(res):       # O(WHlogH), W, H are width and height of the tree
            res[y_pos].sort(key = lambda x: x[0])
            ans.append(val for key, val in res[y_pos])
        return ans
        
    def _find_depth(self, root, depth):
        if not root:
            return depth - 1
        
        left = self._find_depth(root.left, depth + 1)
        right = self._find_depth(root.right, depth + 1)
        
        return max(left, right)
    
    def _find_leftmost(self, root):
        leftmost = 0
        while root.left:
            root = root.left
            leftmost += 1
        return leftmost
    
    def _find_rightmost(self, root):
        rightmost = 0
        while root.right:
            root = root.right
            rightmost += 1
        return rightmost
    
    def _dfs(self, root, x_pos, y_pos, res):
        res[x_pos].append((y_pos, root.val))
        if root.left: self._dfs(root.left, x_pos-1, y_pos+1, res)
        if root.right: self._dfs(root.right, x_pos+1, y_pos+1, res)
