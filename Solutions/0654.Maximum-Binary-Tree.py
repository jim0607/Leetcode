654. Maximum Binary Tree

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1




# solution 1: simple recursion, O(N^2), O(N^2) in worst case: [1,2,3,4,5,6]
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        maxNum = max(nums)
        idx = nums.index(maxNum)
        
        root = TreeNode(maxNum)
        
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx + 1:])
        
        return root
        
# solution 2: monostack
# 通过观察发现规律，对于每个node的父亲节点 = min(左边第一个比它大的，右边第一个比它大的)
# 维护一个降序数组，可以实现对这个min的快速查找, # O(N), O(N)
# [2, 5, 6, 0, 3, 1]
# stack = [2], push 5 因为 5 > 2, 所以2是5的左儿子, pop 2
# stack = [], push 5
# stack = [5], push 6, 因为 6 > 5，所以5是6的左儿子, pop 5
# stack = [], push 6
# stack = [6], push 0, 因为0 < 6, stack = [6], 所以0是6的右儿子
# stack = [6, 0], push 3, 因为3 > 0, 所以0是3的左儿子， pop 0
# stack = [6], 所以3是6的右儿子， push 3
# stack = [6, 3], push 1, 因为1 < 3，所以1是3的右儿子

"""每个node的父亲节点 = min(左边第一个比它大的，右边第一个比它大的)
# 维护一个降序数组，可以实现对这个min的快速查找"""
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        
        st = []     # maintain a mono decreasing stack, the items in the stack are nodes
        for num in nums:
            node = TreeNode(num)    # fisrtly make it a node
            
            while len(st) > 0 and st[-1].val < num:
                node.left = st.pop()
            
            if len(st) > 0:
                st[-1].right = node
                
            st.append(node)
        
        return st[0]
