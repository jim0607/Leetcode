86. Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left_dummy = ListNode(0)
        right_dummy = ListNode(0)
        left_curr, right_curr = left_dummy, right_dummy
        curr = head
        while curr:
            if curr.val < x:
                left_curr.next = curr
                curr = curr.next
                left_curr = left_curr.next
            else:
                right_curr.next = curr
                curr = curr.next
                right_curr = right_curr.next
                
        right_curr.next = None              # 注意这里断开很重要
        left_curr.next = right_dummy.next   # 注意这里要把两边连起来

        return left_dummy.next
