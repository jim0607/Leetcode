#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (36.97%)
# Likes:    2780
# Dislikes: 291
# Total Accepted:    383.5K
# Total Submissions: 1M
# Testcase Example:  '8\n[4,1,8,4,5]\n[5,0,1,8,4,5]\n2\n3'
#
# Write a program to find the node at which the intersection of two singly
# linked lists begins.
# 
# For example, the following two linked lists:
# 
# 
# begin to intersect at node c1.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA =
# 2, skipB = 3
# Output: Reference of the node with value = 8
# Input Explanation: The intersected node's value is 8 (note that this must not
# be 0 if the two lists intersect). From the head of A, it reads as
# [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes
# before the intersected node in A; There are 3 nodes before the intersected
# node in B.
# 
# 
# 
# Example 2:
# 
# 
# 
# Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3,
# skipB = 1
# Output: Reference of the node with value = 2
# Input Explanation: The intersected node's value is 2 (note that this must not
# be 0 if the two lists intersect). From the head of A, it reads as
# [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes
# before the intersected node in A; There are 1 node before the intersected
# node in B.
# 
# 
# 
# 
# Example 3:
# 
# 
# 
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: null
# Input Explanation: From the head of A, it reads as [2,6,4]. From the head of
# B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must
# be 0, while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.
# 
# 
# 
# 
# Notes:
# 
# 
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function
# returns.
# You may assume there are no cycles anywhere in the entire linked
# structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# 
# 
#

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        currA, currB = headA, headB
        while currA != currB:
            if not currA:
                currA = headB
            else:
                currA = currA.next
                
            if not currB:
                currB = headA
            else:
                currB = currB.next
        
        return currA

    
    
"""solution 2: 把headB的头部和尾部连接起来，然后看看headA开始的大链表有没有环就可以了
this solution cannot be accepted because of ERROR: linked structure was modified."""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        if not headA.next or not headB.next:
            return None
        
        # step 1: hook up head and tail of list B
        currB = headB
        while currB.next:
            currB = currB.next
        currB.next = headB
        
        # step 2: use the same method as 142 ot find the position of cycle
        slow, fast = headA.next, headA.next.next
        while slow != fast:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
        
        p1, p2 = headA, slow
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1
