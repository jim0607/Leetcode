252. Meeting Rooms

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true


"""
Solution 1: O(nlogn), O(1). 题目问一个人能不能参加所有的meeting, 
只需要sort the intervals, if intervals[i][0] < intervals[i - 1][1] then return False
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda interval: (interval[0], interval[1]))
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
            
        return True


"""
Solution 2: O(nlogn), O(n). 用meeting room 2的扫描线做法
"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        start = [interval[0] for interval in intervals]
        end = [interval[1] for interval in intervals]
        start.sort()
        end.sort()
        
        i, j = 0, 0
        room_in_use = 0
        while i < len(start) and j < len(end):
            if start[i] < end[j]:
                room_in_use += 1
                if room_in_use >= 2:
                    return False
                i += 1
            else:
                room_in_use -= 1
                j += 1
        
        return True
                
