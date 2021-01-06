"""
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


"""
Append the new interval to the intervals, and then do the 56. merge interval problem
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        
        # below we will just need to do 56. merge interval problem
        intervals.sort(key = lambda interval: (interval[0], interval[1]))   # only the last item is not sorted, to sort a nearly sorted list, we use insertion sort - close to O(N)
        
        merged = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] > res[-1][-1]:
                merged.append(interval)
            else:
                merged[-1][-1] = max(res[-1][-1], interval[1])
        return merged
    
    
"""
O(N) solution. just loop over the interval and check 是不是相交，
如果不相交就直接append到merged，如果相交就expand new_interval
"""
class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        if not intervals:
            return [new_interval]
        
        merged = []
        for i, (start, end) in enumerate(intervals):
            if end < new_interval[0]:
                merged.append([start, end])
                
            elif start > new_interval[1]:
                merged.append(new_interval)     # 注意在这里 append new_interval
                return merged + intervals[i:]
            
            else:       # if there is overlap, we expand the new_interval
                new_interval[0] = min(new_interval[0], start)   
                new_interval[1] = max(new_interval[1], end)
                
        merged.append(new_interval)   # 在这里append new_interval in case new_interval在最右边
                
        return merged

"""
Since the input intervals are well sorted by start time, meaning there is no overlaps in the interval, 
we can do binary Search to find the first start_idx > new_interval.end, and the last end_idx < new_interval.start
However, even with a Binary Search we can't do better than O(n). 
This is due to the fact that we need to merge all overlapping intervals.
"""
    
"""
Facebook follow up:  How do you add intervals and merge them for a large stream of intervals?
Since each insert takes O(N), it is not wise to use list as the data structure.  
BST is a good data structure to enable O(logn) insertion and O(logn) query as well.
We need to have two functions for the tree (add interval and query tree).
https://leetcode.com/problems/merge-intervals/discuss/355318/Fully-Explained-and-Clean-Interval-Tree-for-Facebook-Follow-Up-No-Sorting
"""
    
