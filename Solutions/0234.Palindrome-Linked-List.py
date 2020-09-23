"""
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


"""
题目要求O(n) time and O(1) space: 
我们只能reverse 一半的linked list，先找到中点，然后reverse the left part，最后比较判断是否为panlindrome
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        # find the mid point of the list, at the same time reverse the left part
        prev, curr, fast = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            
            # reverse the left part of the linked list
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # the left part's head is prev, 
        # the right part's head is curr or curr.next depending on even or odd number of nodes
        if not fast:        # even number of nodes
            left, right = prev, curr
        else:               # odd number of nodes
            left, right = prev, curr.next
        
        # check palindrome
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
