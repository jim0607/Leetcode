83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        anchor, curr = head, head.next
        while curr:
            if anchor.val == curr.val:
                anchor.next = curr.next
                curr = curr.next    # 注意curr往前挪，anchor不要往前挪
            else:
                anchor = curr
                curr = curr.next
        
        return head
