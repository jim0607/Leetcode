2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.



"""本题的考点是关于如何新建一个linked list, 要用someNode.next = ListNode(someVal), 而不是简单的修改value
还考察了是否细心"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        curr1, curr2 = l1, l2
        carryBit = 0
        while curr1 and curr2:
            sumVal = curr1.val + curr2.val + carryBit
            curr.next = ListNode(sumVal % 10)   # 光说curr.val = sumVal%10 没用的，curr只是一个局部变量指向一个节点的地址而已，并不是一个节点，只有curr.next才能增加节点。
            carryBit = sumVal // 10

            curr = curr.next
            curr1 = curr1.next
            curr2 = curr2.next
            
        while curr1:                            # 要细心，很容易漏掉
            sumVal = curr1.val + carryBit
            curr.next = ListNode(sumVal % 10)
            carryBit = sumVal // 10
            
            curr = curr.next
            curr1 = curr1.next
        
        while curr2:
            sumVal = curr2.val + carryBit
            curr.next = ListNode(sumVal % 10)
            carryBit = sumVal // 10
            
            curr = curr.next
            curr2 = curr2.next
        
        if carryBit > 0:                        # 这个更容易漏掉
            curr.next = ListNode(carryBit)
            
        return dummy.next 
