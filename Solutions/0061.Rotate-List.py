61. Rotate List

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        
        # step 1: get the lens of the list
        lens = 0
        curr = head
        tail = curr
        while curr:     
            tail = curr     # track where the tial is, will use later
            curr = curr.next
            lens += 1
        
        k = lens - k % lens
        if k == lens:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        prev, curr = dummy, dummy.next
        for _ in range(k):
            prev = prev.next
            curr = curr.next
            
        prev.next = None    # 断开3->4
        tail.next = head    # 连接5->1
        
        return curr
