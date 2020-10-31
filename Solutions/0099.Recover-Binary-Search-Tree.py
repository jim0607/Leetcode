"""
99. Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""


"""
Let's do this problem first: Sort an almost sorted array where only two elements are swapped
Given an almost sorted array where only two elements are swapped, how to sort the array efficiently?
"""
class SortByOneSwap:
    def sort_by_one_swap(self, arr):
        wrong_node_1, wrong_node_2 = None, None
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                wrong_node_2 = i
                if wrong_node_1 == None:
                    wrong_node_1 = i - 1
                else:
                    break
        arr[wrong_node_1], arr[wrong_node_2] = arr[wrong_node_2], arr[wrong_node_1]


if __name__ == "__main__":
    arr = [1,8,3,4,5,6,7,2]
    sol = SortByOneSwap()
    sol.sort_by_one_swap(arr)
    print(arr)
    
    
    
"""
solution 1: do an in order traversal turn it into a list, and then find the swapped elements.
It's not modify in place, we need to modify in-place. 
Think about how do we modify an sorted arr problem in place. 
Similar with the previous mode problem, we need to use a global prev_node, so that we can compare the adjacent nodes in the sorted arr.
"""
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.wrong_node_1 = None
        self.wrong_node_2 = None
        self.prev_node = None
        self.in_order(root)
        self.wrong_node_1.val, self.wrong_node_2.val = self.wrong_node_2.val, self.wrong_node_1.val

    def in_order(self, root):
        if not root:
            return
        
        self.in_order(root.left)
        
        if self.prev_node and root.val < self.prev_node.val:
            if not self.wrong_node_1:
                self.wrong_node_1 = self.prev_node
                self.wrong_node_2 = root    # 这里要赋值second_swapped是因为可能就是相邻的两个nodes交换了
            else:
                self.wrong_node_2 = root
                
        self.prev_node = root               # 注意要改变prev_node
            
        self.in_order(root.right)
