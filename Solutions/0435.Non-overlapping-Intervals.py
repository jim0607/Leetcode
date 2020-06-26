435. Non-overlapping Intervals

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.


"""
This is actually greedy algorithm: always pick the interval with the earliest end time. 
Then you can get the maximal number of non-overlapping intervals. (or minimal number to remove).
Implemented using sweep line: 
Step 1: sort the list based on the end time of the intervals, cuz we want to pick up the earliest end time.
step 2: use a pointer (represent end time) to sweep over the intervals. each time, we compare the pointer with the start time.
if the interval has an start time larger than the pointer, then renew the pointer to be the new end time;
else then we will have to remove the interval in order to to keep the end time as small as possible,  removed_cnt += 1
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # in order to make this algorithm work, we need to sort based on the end time of the intervals
        intervals.sort(key = lambda interval: (interval[1], interval[0]))
        removed_cnt = 0
        end = float("-inf")
        for interval in intervals:
            if interval[0] >= end:
                end = interval[1]
            else:   # if interval[0] < end, then we should remove this interval
                removed_cnt += 1
                
        return removed_cnt
