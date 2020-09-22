82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3



"""
anchor stays where on it's left there is only distinct numbers
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast:
            if fast.val != slow.val:
                slow = slow.next
                slow.val = fast.val
            fast = fast.next
        
        slow.next = None    # 把anchor后面的都断开，因为后面的都是duplicated numbers
        
        return head
