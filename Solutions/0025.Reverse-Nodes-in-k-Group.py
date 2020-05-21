#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (47.54%)
# Likes:    1651
# Dislikes: 146
# Total Accepted:    393K
# Total Submissions: 823.9K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        curr = dummy
        while curr:
            curr = self.reverseK(curr, k)
            
        return dummy.next
    
    def reverseK(self, curr, k):
        """reverse n0->n1->n2------>nk->n_k+1 to be n0->nk------>n2->n1->n_k+1 and return n1"""
        
        # find n0 and n1
        n0 = curr
        n1 = curr.next
        
        # find n_k and n_k_plus
        while k > 0:
            curr = curr.next
            k -= 1
            if not curr:        # if the lens of curr->n1->n2--->None is less than k, then return None
                return None 
            
        n_k = curr
        n_k_plus = curr.next
            
        # reverse n1->n2------>nk to be nk------>n2->n1
        prevNode, currNode = n1, n1.next
        while currNode != n_k_plus:
            temp = currNode.next
            currNode.next = prevNode
            
            prevNode = currNode
            currNode = temp
        
        # hook up n0 with n_k, n1 with n_k+1
        n0.next = n_k
        n1.next = n_k_plus
        
        return n1

    
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        reverse the list started with head
        return new head
        """
        # step 1: exit of recursion: when less than k elements left, return head directly
        if not head or not head.next:
            return head
        currNode = head
        for _ in range(k - 1):
            currNode = currNode.next
            if not currNode:
                return head
            
        # step 2: revursivey find the new head of the reversed list
        nextGroupHead = self.reverseKGroup(currNode.next, k)
        
        # step 3: reverse the first k elements
        dummyNode = ListNode(0)
        dummyNode.next = head
        prev, curr = None, head
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # step 4: hook up the reversedNewHead with head
        head.next = nextGroupHead
        
        return prev
