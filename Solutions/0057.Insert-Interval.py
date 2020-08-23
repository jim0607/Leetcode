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
Solution 2: add the interval on the run O(n).  If there is overlap, we update the new interval.
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        new_start, new_end = newInterval
        for start, end in intervals:
            if end < new_start or start > new_end:
                merged.append([start, end])
            else:       # there is overlap - 更新new interval
                new_start = min(new_start, start)
                new_end = max(new_end, end)
                
        merged.append([new_start, new_end])
        
        return sorted(merged)   # to sort a nearly sorted list, use insertion sort - close to O(N)

    
Facebook follow up:  How do you add intervals and merge them for a large stream of intervals?
Since each insert takes O(N), it is not wise to use list as the data structure.  
BST is a good data structure to enable O(logn) insertion and O(logn) query as well.
We need to have two functions for the tree (add interval and query tree).
https://leetcode.com/problems/merge-intervals/discuss/355318/Fully-Explained-and-Clean-Interval-Tree-for-Facebook-Follow-Up-No-Sorting
    
