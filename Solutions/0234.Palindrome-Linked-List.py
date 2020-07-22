234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?



"""
题目要求O(n) time and O(1) space: 我们只能prev, slow, fast往前走的过程中修改指针指向，
将slow反向指给prev. 
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        if not head.next.next:
            return head.val == head.next.val
        
        # step 1: prev, slow, fast往前走的过程中修改指针指向，将slow反向指给prev. 
        dummy = ListNode(-1)
        dummy.next = head
        prev, slow, fast = dummy, dummy.next, dummy.next.next
        while fast and fast.next:
            temp = slow.next
            slow.next = prev
            
            prev = slow
            slow = temp
            fast = fast.next.next
        
        # step 2: 找到new lefthead new righthead
        temp = slow.next
        if fast:    # even number of nodes
            slow.next = prev
            prev = slow
            
        left, right = prev, temp
        print(left.val, right.val)
        
        # step 3: check panlindrome
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
