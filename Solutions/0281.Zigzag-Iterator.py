281. Zigzag Iterator

Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6] 
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
 

Follow up:

What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].


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
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
