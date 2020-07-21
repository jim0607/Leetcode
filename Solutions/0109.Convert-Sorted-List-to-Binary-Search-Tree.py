109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 
 
 
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        if not head.next.next:
            return TreeNode(head.val, None, TreeNode(head.next.val))
        if not head.next.next.next:
            return TreeNode(head.next.val, TreeNode(head.val), TreeNode(head.next.next.val))
        
        # 找中间节点
        dummy = ListNode(0)
        dummy.next = head
        prev, slow, fast = dummy, dummy.next, dummy.next.next
        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next
        
        # 根据中间节点分成左右两部分
        prev.next = None    # 断掉左边
        righthead = slow.next
        slow.next = None    # 断掉右边
            
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(righthead)
        
        return root




"""
solution 2: 上述方法需要 O(NlogN)的原因是每次寻找中间点mid的时间都是O(N), 我们可以把linked list转化为arr,
这样我们找mid就只需要O(1)了, 这时候再根据Master's theorem: 我们通过O(1)的时间将T(N)的任务变成了2T(N/2)的任务，
所以总的时间复杂度是O(N)
"""
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
            
        return self._constructBST(arr, 0, len(arr)-1)
        
    def _constructBST(self, arr, left, right):
        if left > right:
            return None
        if left == right:
            return TreeNode(arr[left])
        
        mid = (left + right) // 2
        root = TreeNode(arr[mid])
        root.left = self._constructBST(arr, left, mid-1)
        root.right = self._constructBST(arr, mid+1, right)
        
        return root
