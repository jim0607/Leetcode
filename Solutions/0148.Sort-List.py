#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (38.58%)
# Likes:    2038
# Dislikes: 102
# Total Accepted:    225.4K
# Total Submissions: 580.1K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list in O(n log n) time using constant space complexity.
# 
# Example 1:
# 
# 
# Input: 4->2->1->3
# Output: 1->2->3->4
# 
# 
# Example 2:
# 
# 
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""解法一：bottom up merge sort
O(NlogN), O(1)"""
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """return the head of the the sorted list"""
        if not head or not head.next:
            return head
        
        # step 1: divide
        midNode = self.findMid(head)
        
        # cut into left and right halfs
        leftHead = head
        
        rightHead = midNode.next
        midNode.next = None
        
        # then we sort the left and right list - divide
        leftHead = self.sortList(leftHead)
        rightHead = self.sortList(rightHead)
        
        # conquer/merge
        newHead = self.merge(leftHead, rightHead)
        
        return newHead
    
    def findMid(self, head):
        """return the midNode of the list"""
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def merge(self, leftHead, rightHead):
        """return the new head after the merge"""
        if not leftHead:
            return rightHead
        if not rightHead:
            return leftHead
        
        dummy = ListNode(0)
        curr = dummy
        leftCurr, rightCurr = leftHead, rightHead
        while leftCurr and rightCurr:
            if leftCurr.val < rightCurr.val:
                curr.next = leftCurr
                leftCurr = leftCurr.next
                curr = curr.next
            else:
                curr.next = rightCurr
                rightCurr = rightCurr.next
                curr = curr.next
                
        while leftCurr:
            curr.next = leftCurr
            leftCurr = leftCurr.next
            curr = curr.next
        while rightCurr:
            curr.next = rightCurr
            rightCurr = rightCurr.next
            curr = curr.next
        
        return dummy.next


"""解法二 is trivial：把ListNode都放到arr中，然后sort arr, 然后再把值放到ListNode中
O(NlogN), O(N)"""
"""class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        # 把listNode放到arr中 O(N)
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        # merge sort the arr
        self._merge_sort_(arr)

        # 然后再把值放到ListNode中
        curr = head
        i = 0
        while curr:
            curr.val = arr[i]
            i += 1
            curr = curr.next

        return head

    def _merge_sort_(self, arr):
        lens = len(arr)
        if lens <= 1:
            return arr
        
        # divide
        mid = lens // 2
        leftArr = self._merge_sort_(arr[:mid])
        rightArr = self._merge_sort_(arr[mid:])

        # conquer/merge
        i, j, k = 0, 0, 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
                k += 1
            else:
                arr[k] = rightArr[j]
                j += 1
                k += 1
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1
        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1

        return arr"""



