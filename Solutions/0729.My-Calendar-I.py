729. My Calendar I

Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

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
solution 1: sweep line just like the airplane in the sky problem - need to sort, so O(nlogn) - TLE
"""
class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        if not self.calendar:
            self.calendar.append([start, end])
            return True
        
        start_lst = [event[0] for event in self.calendar]
        start_lst.append(start)
        start_lst.sort()
        end_lst = [event[1] for event in self.calendar]
        end_lst.append(end)
        end_lst.sort()
        
        i, j = 0, 0
        cnt = 0
        while i < len(start_lst) and j < len(end_lst):
            if start_lst[i] < end_lst[j]:
                cnt += 1
                i += 1
            else:
                cnt -= 1
                j += 1
                
            if cnt >= 2:
                return False
            
        if cnt >= 2:
            return False
        
        self.calendar.append([start, end])
        
        return True


                                                                                                                          
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
            

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
