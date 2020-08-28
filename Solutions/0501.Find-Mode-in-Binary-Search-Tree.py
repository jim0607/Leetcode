501. Find Mode in Binary Search Tree

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.


"""
solution 1: dfs to visit every node and put their freq in a dict - O(N), O(N)
"""
"""
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        
        def dfs(root):
            if not root:
                return
            
            freq[root.val] += 1
                
            dfs(root.left)
            dfs(root.right)
        
        
        freq = collections.defaultdict(int)
        dfs(root)
        max_freq = max(f for f in freq.values())
        
        return [key for key, f in freq.items() if f == max_freq]
        
        
"""
Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""
"""
Before we do the follow up question for BST. Let's think how to do it in a sorted arr with O(1) space.
We dynamically update the curr_cnt and max_cnt and res, by comparing prev with curr.
"""
class ModeInSortedArr:

    def find_mode(self, arr):
        prev = None
        curr_cnt = 1
        max_cnt = 1
        res = []

        for i, num in enumerate(arr):
            curr_cnt = curr_cnt + 1 if num == prev else 1   # 如果不相等就reset curr_cnt=1
            if curr_cnt == max_cnt:
                res.append(num)
            elif curr_cnt > max_cnt:
                res = [num]
                max_cnt = curr_cnt
            prev = num

        return res

if __name__ == "__main__":
    arr = [1,2,2,2,3,3,4,5,5,5,6,6]
    sol = ModeInSortedArr()
    print(sol.find_mode(arr))
    
    
    
    
"""
solving BST problems is very similar with solving sorted arr problems.
we just need to do in order traversal of the tree.
O(N), O(1)
"""

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        self.prev = None
        self.max_cnt = 1
        self.curr_cnt = 1
        self.res = []
        
        self.inorder(root)
        return self.res
        
    def inorder(self, root):    # in order traversal the BST and update the res, just like doing everything in a sorted arr
        if not root:
            return 
        
        self.inorder(root.left)
        
        self.curr_cnt = self.curr_cnt + 1 if root.val == self.prev else 1   # 如果不相等就reset curr_cnt=1
        if self.curr_cnt == self.max_cnt:
            self.res.append(root.val)
        elif self.curr_cnt > self.max_cnt:
            self.res = [root.val]               # 这里更新res的时候要清除之前的items
            self.max_cnt = self.curr_cnt
        self.prev = root.val
        
        self.inorder(root.right)
        
"""
特别注意下面写法是不对的，不能把prev_node传进去
""
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        def helper(root, prev):
            if not root:
                return
            
            helper(root.left, root)   
            
            if prev and root.val == prev.val:
                self.curr_cnt += 1
            else:
                self.curr_cnt == 1
                
            if self.curr_cnt == self.max_cnt:    
                self.res.append(root.val)
            elif self.curr_cnt > self.max_cnt:
                self.res = [root.val]
                self.max_cnt = self.curr_cnt
            
            helper(root.right, root)    # 这里是不对的

            
        self.curr_cnt = 1
        self.max_cnt = 1
        self.res = []
        
        helper(root, None)
        
        return self.res
