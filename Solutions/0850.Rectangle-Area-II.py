850. Rectangle Area II

We are given a list of (axis-aligned) rectangles.  Each rectangle[i] = [x1, y1, x2, y2] , where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane.  Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
Example 2:

Input: [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
Note:

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= rectangles[i][j] <= 10^9
The total area covered by all rectangles will never exceed 2^63 - 1 and thus will fit in a 64-bit signed integer.


"""
sweep line solution: O(N^2logN).
This is two sweep line problem pieced together.
https://www.youtube.com/watch?v=xm5-u_l8tTY
"""
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        INT_MIN = -2 ** 32
        
        # convert list of rectangles to events
        events = [] # tuple of x, type, y1, y2
        for x1, y1, x2, y2 in rectangles:
            events.append([x1, 0, y1, y2])
            events.append([x2, 1, y1, y2])
        events.sort(key = lambda x: x[0])
            
        # helper function to do total interval lentgh via sweeop line
        def gain_area(m):
            area = 0
            prev = INT_MIN
            for left, right in open_intervals:
                prev = max(prev, left)
                area += max(0, (right - prev) * m)   # avoid the duplicate area
                prev = max(right, prev)
            return area
        
        # sweep line to realize area
        area = 0
        prev = INT_MIN
        open_intervals = []
        for event in events:
            curr, close, y1, y2 = event
            area += gain_area(curr - prev)
            if close:
                open_intervals.remove((y1, y2))
            else:
                open_intervals.append((y1, y2))
                open_intervals.sort()
            prev = curr
        return area % MOD





When I update the coverage on x, I updated one by one.
But in fact I update for a range.
If we use a segment tree to update the coverage, it will be only O(logN) for add and delete action.
The overall time complexity would be O(NlogN). Not ganna implement it in an interview.
