"""
452. Minimum Number of Arrows to Burst Balloons

There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
"""


"""
Step 1: sort the intervals by end time;
Step 2: sweep line: use a pointer representing the end time, at each interval, we compare the pointer with the interval start time.
if end >= interval start time: then there is overlap and we should wait so that later we can shot them together;
if end > interval start time, then we can shot the previously 积累下来的interveals, shots += 1, and move the end to the new interval end time
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[1], x[0]))
        
        min_end = -sys.maxsize
        shots = 0
        for start, end in points:
            if start <= min_end:
                min_end = min(min_end, end)
            else:
                shots += 1
                min_end = end
        return shots
