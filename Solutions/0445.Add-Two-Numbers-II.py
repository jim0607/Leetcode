445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7



"""
step 1: reverse the list;
step 2: do exactly the same as LC 2. Add Two Numbers;
step 3: reversse back
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        reversed_head1, reversed_head2 = self._reverse(l1), self._reverse(l2)
        
        dummy = ListNode(0)
        curr = dummy
        curr1, curr2 = reversed_head1, reversed_head2
        carry_bit = 0
        while curr1 and curr2:
            sums = curr1.val + curr2.val + carry_bit
            carry_bit = sums // 10
            curr.next = ListNode(sums % 10)
            curr = curr.next
            curr1 = curr1.next
            curr2 = curr2.next
        while curr1:
            sums = curr1.val + carry_bit
            carry_bit = sums // 10
            curr.next = ListNode(sums % 10)
            curr = curr.next
            curr1 = curr1.next
        while curr2:
            sums = curr2.val + carry_bit
            carry_bit = sums // 10
            curr.next = ListNode(sums % 10)
            curr = curr.next
            curr2 = curr2.next
        while carry_bit != 0:
            sums = carry_bit
            carry_bit = sums // 10
            curr.next = ListNode(sums % 10)
            curr = curr.next
        
        temp = dummy.next
        dummy.next = None   # 把dummy与已经建好的List断开
        head = self._reverse(temp)
        
        return head
    
    def _reverse(self, head):
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
