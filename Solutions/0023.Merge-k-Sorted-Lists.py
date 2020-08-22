23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6


solution 1: heapq
O(NlogK), O(K)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import *

class Solution:
    # first, we should overriding ListNode compare function __lt__ to make customized compare happens: compare ListNode
    def __lt__(self, other):        # re-define the __lt__ function
        return self.val < other.val
    
    ListNode.__lt__ = __lt__        # overide the __lt__ function for ListNode
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        hq = []
        for head in lists:
            if head:
                heappush(hq, head)
            
        dummynode = ListNode(0)
        curr = dummynode
        while len(hq) > 0:
            curr.next = heappop(hq)
            curr = curr.next
            if curr.next:
                heappush(hq, (curr.next))
                
        return dummynode.next
      
      
"""
soluiton 2: divide and conquer
time complexity: each merge takes N operations and we divide/merge logk times, so it's O(Nlogk)
"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        # divide
        mid = len(lists) // 2
        lefthead = self.mergeKLists(lists[:mid])
        righthead = self.mergeKLists(lists[mid:])
        
        # conquer/merge
        dummy = ListNode(0)
        curr = dummy
        leftcurr, rightcurr = lefthead, righthead
        while leftcurr and rightcurr:
            if leftcurr.val < rightcurr.val:
                curr.next = leftcurr
                curr = curr.next
                leftcurr = leftcurr.next
            else:
                curr.next = rightcurr
                curr = curr.next
                rightcurr = rightcurr.next
        curr.next = leftcurr if leftcurr else rightcurr
        
        return dummy.next
