Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root):
            """
            return (the maxVal, minVal, isValid) for the tree rooted as root
            """
            if not root:
                return (-float("inf"), float("inf"), True)
            
            leftMax, leftMin, leftIsValid = helper(root.left)
            rightMax, rightMin, rightIsValid = helper(root.right)
            
            rootMax = max(leftMax, rightMax, root.val)  # # 最开始写找半天错误，最后发现是忘了把root.val加入比较了，本质是忘了递归的定义：返回root为根的树(是不是BST，max and min value in the tree)，想想bottom up的时候这一层算出来的max是要被上面的一层拿出来用的。
        else:
            return False, max(maxLeft, maxRight, root.val), min(minLeft, minRight, root.val)

Time complexity : O(N) since we visit each node exactly once.
Space complexity : O(N) since we keep up to the entire tree.

            rootMin = min(leftMin, rightMin, root.val)
            rootIsValid = leftIsValid and rightIsValid and (leftMax < root.val < rightMin)
            
            return (rootMax, rootMin, rootIsValid)
        
        return helper(root)[2]

Time complexity : O(N) since we visit each node exactly once.
Space complexity : O(N) since we keep up to the entire tree.
