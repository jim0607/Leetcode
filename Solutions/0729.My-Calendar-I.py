"""
729. My Calendar I

Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), 
the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. 
Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
"""


"""
solution 1:一个interval与另一个interval的位置关系就三种情况(1. 没有交集; 2. 一个包含了另一个; 3. 有交集但是没有谁能完全包含谁). 
这里我们只要遇到case 2 or case 3, then there is an overlap, return False
"""
class MyCalendar:

    def __init__(self):
        self.intervals = [[-1, -1]]

    def book(self, start: int, end: int) -> bool:
        for interval in self.intervals:
            # 一个interval与另一个interval的位置关系就三种情况
            # (1. 没有交集; 2. 一个包含了另一个; 3. 有交集但是没有谁能完全包含谁)
            # 这里我们只要遇到case 2 or case 3, then there is an overlap, return False
            if not (interval[0] >= end or interval[1] <= start):
                return False
                
        self.intervals.append([start, end])
            
        return True


"""
binary search tree - O(logN)
"""
class TreeNode:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class MyCalendar:

    def __init__(self):
        self.root = None
        
    def insert(self, start, end, root):
        """
        insert an interval into a root (not self.root), return whether or not it could be inserted
        """
        if start >= root.end:
            if root.right:
                return self.insert(start, end, root.right)
            else:
                root.right = TreeNode(start, end)
                return True
        elif end <= root.start:
            if root.left:
                return self.insert(start, end, root.left)
            else:
                root.left = TreeNode(start, end)
                return True
        else:
            return False

    def book(self, start: int, end: int) -> bool:       # O(logN) on random data. O(N) if the tree is highly un-balanced
        if not self.root:
            self.root = TreeNode(start, end)
            return True
        return self.insert(start, end, self.root)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
    
    
    
    

                                                                                                                          
"""
solution 2: binary search where the interval should be inserted and insert the interval, so O(n + logn)
"""
class MyCalendar:

    def __init__(self):
        self.calendar = []      # maintain a sorted list

    def book(self, start: int, end: int) -> bool:
        if not self.calendar:
            self.calendar.append([start, end])
            return True
        
        if start >= self.calendar[-1][-1]:
            self.calendar.append([start, end])
            return True
        
        if end <= self.calendar[0][0]:
            self.calendar.insert(0, [start, end])
            return True
        
        # below we will binary search where the start should be located
        lens = len(self.calendar)
        left, right = 0, lens - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if start <= self.calendar[mid][0]:
                right = mid
            else:
                left = mid
        idx = left if self.calendar[left][0] > start else right

        # after found where the idx should be located, we should check if [start, end] could fit in
        if start < self.calendar[idx-1][1]:
            return False
        if end > self.calendar[idx][0]:
            return False
        
        # if [start, end] can fit in, we insert it at the idx we found - O(N)
        self.calendar.insert(idx, [start, end])
        return True
            

"""
solution 3: we can try to implement a balanced tree (maybe a red-black tree) to enable O(logn) insert and O(logn) search.  But it is way too complicated. 
"""
                                                                                                                          
