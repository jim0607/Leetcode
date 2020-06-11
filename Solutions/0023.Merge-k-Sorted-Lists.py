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

class Solution:
    # first, we should overriding ListNode compare function __lt__ to make customized compare happens: compare ListNode
    def __lt__(self, other):
        return self.val < other.val
    
    ListNode.__lt__ = __lt__
  
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists == [None]:
            return None
        
        dummyNode = ListNode(0)
        curr = dummyNode
        
        import heapq
        
        hq = []
        for head in lists:
            if head:
                heapq.heappush(hq, head)
 
        while hq:
            minNode = heappop(hq)
            curr.next = minNode
            curr = curr.next
            
            if minNode.next:
                heapq.heappush(hq, minNode.next)
                
        return dummyNode.next
      
      
"""
soluiton 2: divide and conquer
time complexity: each merge takes N operations and we divide/merge logk times, so it's O(Nlogk)
"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        # divide
        mid = len(lists) // 2
        leftHead = self.mergeKLists(lists[:mid])
        rightHead = self.mergeKLists(lists[mid:])
        
        # conquer/merge
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
        curr.next = leftCurr if leftCurr else rightCurr
        
        return dummy.next
