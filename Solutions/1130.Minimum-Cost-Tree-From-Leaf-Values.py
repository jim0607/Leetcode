1130. Minimum Cost Tree From Leaf Values

Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.

 

Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4



"""
The main idea is that you want to use the two smallest as leaf nodes to construct a root node. 
So, here we loop through the entire array, whenever we find stack[-1] <= currNum, 
which means that this top element stack[-1] is a local minimum. 
So we use this element with its left or right to construct a root node. (res += min(drop * currNum, drop * stack[-1])). You can think this is a greedy algorithm.
"""
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        st = [float("inf")]     # 给个初始值垫底，防止st变空
        res = 0
        for num in arr:
            while st and st[-1] <= num:
                top = st.pop()
                res += top * min(num, st[-1])
            st.append(num)
            
        while len(st) > 2:      
            top = st.pop()
            res += top * st[-1]   # 这里的st[-1]会用到两次是因为与top构建root的左子树需要用一次，然后在下一个循环里把下一个next st[-1]放在root的右子树里，计算root又需要用一次
            
        return res
