759. Employee Free Time

We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

 

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]



"""
这题是merge interval的变形题: 
step 1: obtain all intervals of all employees;
step 2: sort the intervals by start time;  
step 3: do 56. merge intervals, to update free time.
"""

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # step 1: obtain all intervals of all employees
        intervals = []
        for employee in schedule:
            for interval in employee:
                intervals.append((interval.start, interval.end))
        
        # step 2: sort the intervals by start time
        intervals.sort()
        
        # step 3: do 56. merge intervals, to update free time. how to do?
        # maintain an end_time as we loop over intervals.
        # if curr start time > end_time, update free time and end_time
        # if curr start <= end_time, update end_time
        free = []
        end_time = intervals[0][1]
        for start, end in intervals:
            if start > end_time:
                free.append([end_time, start])
                end_time = end
            else:
                end_time = max(end_time, end)
                
        return [Interval(start, end) for start, end in free]    # 把list转换成Interval Obj
