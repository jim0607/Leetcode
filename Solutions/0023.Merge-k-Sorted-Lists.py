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



O(NlogK), O(K)

# overwrite the compare function 
# so that we can directly put ListNode into heapq
ListNode.__lt__ = lambda x, y: (x.val < y.val)

class Solution:
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
