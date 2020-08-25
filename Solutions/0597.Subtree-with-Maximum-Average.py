Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum average.

Have you met this question in a real interview?  
Example
Example 1

Input：
{1,-5,11,1,2,4,-2}
Output：11
Explanation:
The tree is look like this:
     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2 
The average of subtree of 11 is 4.3333, is the maximun.


class Solution:
    def findSubtree2(self, root):
        if not root:
            return None
            
        self.max_avg = float("-inf")
        self.max_root = root
        self._helper(root)
        
        return self.max_root
        
    def _helper(self, root):
        """
        return the how many nodes are there for the subtree and the subree sum
        """
        if not root:
            return 0, 0
        
        # divide
        left_cnt, left_sum = self._helper(root.left)
        right_cnt, right_sum = self._helper(root.right)
        
        # conquer
        cnt = left_cnt + right_cnt + 1
        sum = left_sum + right_sum + root.val
        avg = sum / cnt
        
        # traverse to conpare, 打擂台
        if avg > self.max_avg:
            self.max_avg = avg
            self.max_root = root
            
        return cnt, sum
