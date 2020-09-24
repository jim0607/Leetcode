"""
Given two binary search trees, return True if and only if there is a node in the first tree 
and a node in the second tree whose values sum up to a given integer target.
Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.
Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false
"""



"""
solution 2: binary tree traversal using iterative way and store the val in a hash map; time complexity: O(M + N)
"""
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        # step 1: put the node of 1st tree into a hash set
        hashset = set()
        curr = root1
        st = []
        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            hashset.add(curr.val)
            curr = curr.right      
        
        # step 2: loop over the 2nd tree and see if there is a node add up to target
        curr = root2
        st = []
        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            if target - curr.val in hashset:
                return True
            curr = curr.right
        return False

    
"""
solution 2: in-order-traversal + 反向双指针
"""  
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        arr_1 = self.in_order_trav(root1)
        arr_2 = self.in_order_trav(root2)
        idx_1, idx_2 = 0, len(arr_2) - 1
        while idx_1 < len(arr_1) and idx_2 >= 0:
            if arr_1[idx_1] + arr_2[idx_2] > target:
                idx_2 -= 1
            elif arr_1[idx_1] + arr_2[idx_2] < target:
                idx_1 += 1
            else:
                return True
            
        return False
    
    def in_order_trav(self, root):
        """
        return a list which is in-order-traversal of BST
        """
        if not root:
            return []
        
        res = []
        res += self.in_order_trav(root.left)
        res.append(root.val)
        res += self.in_order_trav(root.right)
        
        return res

    
    
"""
Brutal force - O(MN) TLE
"""
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if not root1 or not root2:
            return False
        if root1.val + root2.val > target:
            return self.twoSumBSTs(root1.left, root2, target) or self.twoSumBSTs(root1, root2.left, target)
        elif root1.val + root2.val < target:
            return self.twoSumBSTs(root1.right, root2, target) or self.twoSumBSTs(root1, root2.right, target)
        else:
            return True
