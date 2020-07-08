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
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


"""
这题是merge interval的变形题，第一步先sort所有的intervals, 然后去找所有非公共的intervals.
"""
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        event = []
        for employee in schedule:
            for interval in employee:
                event.append((interval.start, interval.end))
                
        event.sort(key = lambda interval: (interval[0], interval[1]))   # O(NlogN), where N is number of total intervals
        
        res = []
        end_time = event[0][0]
        for interval in event:
            if interval[0] > end_time:
                res.append([end_time, interval[0]])
                end_time = interval[1]
            else:
                end_time = max(end_time, interval[1])
         
        ans = []
        for interval in res:
            ans.append(Interval(interval[0], interval[1]))  # 把list转换成Interval Obj
            
        return ans
