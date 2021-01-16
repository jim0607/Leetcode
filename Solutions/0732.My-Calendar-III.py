"""
732. My Calendar III

Implement a MyCalendarThree class to store your events. A new event can always be added.

Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A K-booking happens when K events have some non-empty intersection (ie., there is some time that is common to all K events.)

For each call to the method MyCalendar.book, return an integer K representing the largest integer such that there exists a K-booking in the calendar.

Your class will be called like this: MyCalendarThree cal = new MyCalendarThree(); MyCalendarThree.book(start, end)
Example 1:

MyCalendarThree();
MyCalendarThree.book(10, 20); // returns 1
MyCalendarThree.book(50, 60); // returns 1
MyCalendarThree.book(10, 40); // returns 2
MyCalendarThree.book(5, 15); // returns 3
MyCalendarThree.book(5, 10); // returns 3
MyCalendarThree.book(25, 55); // returns 3
Explanation: 
The first two events can be booked and are disjoint, so the maximum K-booking is a 1-booking.
The third event [10, 40) intersects the first event, and the maximum K-booking is a 2-booking.
The remaining events cause the maximum K-booking to be only a 3-booking.
Note that the last event locally causes a 2-booking, but the answer is still 3 because
eg. [10, 20), [10, 40), and [5, 15) are still triple booked.
"""


"""
Maintain a start_time list and end_time list and keep them sorted by using binary search each time we insert a time.
Do do exactly the same as the airplane in the sky problem. O(N)
"""
class MyCalendarThree:

    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> int:
        # step 1: binary search to find where the time should be inserted and insert into the left and right list - O(N)
        start_idx = bisect.bisect_left(self.starts, start)
        self.starts.insert(start_idx, start)
        end_idx = bisect.bisect_left(self.ends, end)
        self.ends.insert(end_idx, end)
        
        # step 2: airplane in the sky problem
        i, j = 0, 0
        max_overlap = 0
        curr_overlap = 0
        while i < len(self.starts) and j < len(self.ends):
            if self.starts[i] < self.ends[j]:
                curr_overlap += 1
                i += 1
            else:
                curr_overlap -= 1
                j += 1
            max_overlap = max(max_overlap, curr_overlap)
        return max_overlap


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
             
                             
                             
"""
另一种写法把binary search 写出来了
"""
class MyCalendarThree:

    def __init__(self):
        self.start_time = []
        self.end_time = []

    def book(self, start: int, end: int) -> int:
        if not self.start_time:
            self.start_time.append(start)
            self.end_time.append(end)
            return 1
        
        # binary search to find where the time should be inserted and insert into the start_time and end_time list - O(N)
        start_idx = self._binary_search(start, self.start_time)
        end_idx = self._binary_search(end, self.end_time)
        self.start_time.insert(start_idx, start)
        self.end_time.insert(end_idx, end)
        
        # now let's do sweep line - O(N)
        k, max_k = 0, 0
        i, j = 0, 0
        while i < len(self.start_time) and j < len(self.end_time):
            if self.start_time[i] < self.end_time[j]:
                k += 1
                i += 1
            elif self.start_time[i] > self.end_time[j]:
                k -= 1
                j += 1
            else:
                i += 1
                j += 1
            max_k = max(max_k, k)
                
        return max_k
        
    def _binary_search(self, target, lst):
        if target <= lst[0]:
            return 0
        if target >= lst[-1]:
            return len(lst)
        
        left, right = 0, len(lst) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if target <= lst[mid]:
                right = mid
            else:
                left = mid
        return left if lst[left] >= target else right


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
