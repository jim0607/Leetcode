"""
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
"""



"""
正解 soluiton 1: divide and conquer
time complexity: each merge takes N operations and we divide/merge logk times, so it's O(Nlogk)
"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        # divide
        mid = len(lists) // 2
        left_head = self.mergeKLists(lists[:mid])
        right_head = self.mergeKLists(lists[mid:])
        
        # conquer/merge - same as 21. Merge Two Sorted Lists
        dummy = ListNode()
        curr = dummy
        left, right = left_head, right_head
        while left and right:
            if left.val < right.val:
                curr.next = ListNode(left.val)
                left = left.next
                curr = curr.next
            else:
                curr.next = ListNode(right.val)
                right = right.next
                curr = curr.next
        curr.next = left if left != None else right
        
        return dummy.next

      
      
"""
solution 2: heapq
O(NlogK), O(K)
"""
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
