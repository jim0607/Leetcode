515. Find Largest Value in Each Tree Row

You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]



class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            lens = len(q)
            max_val = float("-inf")
            for _ in range(lens):
                curr = q.popleft()
                max_val = max(max_val, curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(max_val)
            
        return res
