21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        curr1, curr2 = l1, l2
        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr = curr.next
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr = curr.next
                curr2 = curr2.next
        while curr1:
            curr.next = curr1 
            curr = curr.next
            curr1 = curr1.next
        while curr2:
            curr.next = curr2
            curr = curr.next
            curr2 = curr2.next
            
        return dummy.next
        
