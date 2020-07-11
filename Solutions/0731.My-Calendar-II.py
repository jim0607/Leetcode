731. My Calendar II

Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
Explanation: 
The first two events can be booked.  The third event can be double booked.
The fourth event (5, 15) can't be booked, because it would result in a triple booking.
The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.



"""
We maintain a calendar list and a overlap list. In book method, we first check if [start, end] is in an overlap,
if it is, then we return False directly.
If it's not, then we return True, before return true, we should update the calendar list and overlap list accordingly.
update calendar: just append [start, end] cuz we don't need the calendar be sorted.
update overlap: find where the overlap is by go through the calendar list, and update it.
"""
"""
class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        # first check if [start, end] is in an overlap
        for overlap_start, overlap_end in self.overlaps:
            if start < overlap_end and end > overlap_start:
                return False
            
        # if not in an overlap, meaing it can either form a 2-fold overlap with others or form no overlap with others
        for start_time, end_time in self.calendar:  # update overlaps list
            if start < end_time and end > start_time:
                self.overlaps.append([max(start, start_time), min(end, end_time)])  # append the overlap part
                
        self.calendar.append([start, end])          # update calendar list
        
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
