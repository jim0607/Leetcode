57. Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].



"""
Append the new interval to the intervals, and then do the merge interval problem
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        
        # below we will just need to do the merge interval problem
        intervals.sort(key = lambda interval: (interval[0], interval[1]))
        
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] > res[-1][-1]:
                res.append(interval)
            else:
                res[-1][-1] = max(res[-1][-1], interval[1])
        
        return res
