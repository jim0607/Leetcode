1272. Remove Interval

Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] represents the set of real numbers x such that a <= x < b.

We remove the intersections between any interval in intervals and the interval toBeRemoved.

Return a sorted list of intervals after all such removals.

 

Example 1:

Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]
Example 2:

Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]
 

Constraints:

1 <= intervals.length <= 10^4
-10^9 <= intervals[i][0] < intervals[i][1] <= 10^9


"""
一个interval与另一个interval的位置关系就六种情况，一一讨论就可以了
"""

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        r_start, r_end = toBeRemoved[0], toBeRemoved[1]
        
        for start, end in intervals:
            
            # 两不相交
            if end <= r_start:
                res.append([start, end])
            elif start >= r_end:
                res.append([start, end])
                
            # 相互包含
            elif start >= r_start and end <= r_end:
                continue
            elif start < r_start and end > r_end:
                res.append([start, r_start])
                res.append([r_end, end])
                
            # 普通相交
            elif r_start < end <= r_end:
                res.append([start, r_start])
            elif r_start <= start < r_end:
                res.append([r_end, end])

        return res
