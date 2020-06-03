281. Zigzag Iterator

Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6] 
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
 

Clarification for the follow up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].

"""
"""Solution: two pointers"""
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.index1 = 0
        self.index2 = 0
        self.bool = True       # True means we can call v1 now
        self.v1 = v1
        self.v2 = v2

    def next(self) -> int:
        if not self.hasNext:
            return None
        
        if (self.bool and self.index1 < len(self.v1)) or self.index2 == len(self.v2):
            item = self.v1[self.index1]
            self.index1 += 1
            self.bool = not self.bool
        
        else:
            item = self.v2[self.index2]
            self.index2 += 1
            self.bool = not self.bool
            
        return item            

    def hasNext(self) -> bool:
        if self.index1 < len(self.v1) or self.index2 < len(self.v2):
            return True
        
        return False
        

Follow up:

What if you are given k 1d vectors? How well can your code be extended to such cases?

Maybe we can use a list = [True] * k to represent whether or not the kth list has been chosen?


"""
To answer follow up question:
We append all the list into one deque. Every time we call next(), we pop a list first, then pop the first num from the list, 
and then re-add it to the end to deque so that we can call it again after k next calls.
"""
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.dq = collections.deque()
        if v1:
            self.dq.append(v1)
        if v2:
            self.dq.append(v2)

    def next(self) -> int:
        if self.hasNext:
            topLst = self.dq.popleft()
            topNum = topLst.pop(0)
            if topLst:
                self.dq.append(topLst)
                
            return topNum

    def hasNext(self) -> bool:
        return len(self.dq) != 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
