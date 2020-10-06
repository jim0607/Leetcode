"""
593. Valid Square

Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
 
Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
"""


"""
看对角线吧 - 平分且相等且垂直
"""
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = []
        for p in [p1, p2, p3, p4]:
            points.append((p[0], p[1]))
        points.sort(key = lambda x: (x[1], x[0]))
        
        x0, y0 = points[0]
        x1, y1 = points[1]
        x2, y2 = points[2]
        x3, y3 = points[3]
        diagnal_x_center1, diagnal_y_center1 = (x0 + x3) / 2, (y0 + y3) / 2
        diagnal_x_center2, diagnal_y_center2 = (x1 + x2) / 2, (y1 + y2) / 2
        diagnal_len1 = (x3 - x0)**2 + (y3 - y0)**2
        diagnal_len2 = (x2 - x1)**2 + (y2 - y1)**2
        if diagnal_x_center1 != diagnal_x_center2 or diagnal_y_center1 != diagnal_y_center2:
            return False
        if diagnal_len1 != diagnal_len2 or diagnal_len1 == diagnal_len2 == 0:
            return False
        if x0 == x3:
            return y1 == y2
        elif x1 == x2:
            return y0 == y3
        elif y1 == y2:
            return x0 == x3
        elif y0 == y3:
            return x1 == x2
        return ((y3 - y0) * (y2 - y1)) / ((x3 - x0) * (x2 - x1)) == -1
