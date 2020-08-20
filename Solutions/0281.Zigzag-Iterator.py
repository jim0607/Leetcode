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
        self.idx1 = 0
        self.idx2 = 0
        self.flag = True    # flag = True means take from v1
        self.v1 = v1
        self.v2 = v2

    def next(self) -> int:
        if self.hasNext():
            if self.idx2 >= len(self.v2) or (self.flag and self.idx1 < len(self.v1)):
                res = self.v1[self.idx1]
                self.idx1 += 1
                self.flag = not self.flag
            elif self.idx1 >= len(self.v1) or (not self.flag and self.idx2 < len(self.v2)):
                res = self.v2[self.idx2]
                self.idx2 += 1
                self.flag = not self.flag
            
            return res

    def hasNext(self) -> bool:
        if self.idx1 >= len(self.v1) and self.idx2 >= len(self.v2):
            return False        
        return True
        

Follow up:

What if you are given k 1d vectors? How well can your code be extended to such cases?

Maybe we can use a list = [True] * k to represent whether or not the kth list has been chosen?


"""
To answer follow up question:
We append all the list into one q. Every time we call next(), we pop a list first, then pop the first num from the list, 
and then re-add it to the end to deque so that we can call it again after k next calls.
"""
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.q = collections.deque()
        if len(v1) > 0: self.q.append(v1[::-1])
        if len(v2) > 0: self.q.append(v2[::-1])
        
    def next(self) -> int:
        if self.hasNext():
            lst = self.q.popleft()
            res = lst.pop()
            if len(lst) > 0:
                self.q.append(lst)
            return res
        
    def hasNext(self) -> bool:
        return len(self.q) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
