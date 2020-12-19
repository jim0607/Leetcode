"""
203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""



class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        anchor, curr = dummy, head      # anchor keeps all not_equal_val nodes on its left
        while curr:
            if curr.val != val:
                anchor.next = curr
                anchor = anchor.next
                curr = curr.next
            else:
                curr = curr.next
        anchor.next = None      # 注意最后要指向None
        return dummy.next
