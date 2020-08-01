1288. Remove Covered Intervals

Given a list of intervals, remove all intervals that are covered by another interval in the list. Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.

 
Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.



"""
sort the intervals by the start time. Then compare each interval with previous intervals,
to see if curr interval has a smaller end time than any of the previous intervals.
we only need to compare with the largest end time in previous intervals.
we can maintain a hq for the end time of the previous intervals 
"""

from heapq import heappush, heappop

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))   # 注意这里要按end_time逆序排列，因为我们希望max_end time go first

        max_end = []
        for start, end in intervals:
            if not max_end or end > -max_end[0][0]:    # should not be removed
                heappush(max_end, (-end, start))
            
        return len(max_end)
