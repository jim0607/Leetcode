Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values 
of the original tree that are greater than or equal to node.val.


"""do a in order traversal (reversed version) to keep track the sums"""

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        stack = []
        curr = root
        addVal = 0
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.right       # reverse the in order traversal (output right nodes first)
                
            curr = stack.pop()  
            
            curr.val += addVal
            addVal = curr.val
            
            curr = curr.left
            
        return root
