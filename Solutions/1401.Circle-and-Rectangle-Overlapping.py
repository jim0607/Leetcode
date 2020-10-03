"""
1401. Circle and Rectangle Overlapping

Given a circle represented as (radius, x_center, y_center) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) 
are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return True if the circle and rectangle are overlapped otherwise return False.

In other words, check if there are any point (xi, yi) such that belongs to the circle and the rectangle at the same time.

Example 1:
Input: radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0) 
Example 2:
Input: radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
Output: true
Example 3:
Input: radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3
Output: true
Example 4:
Input: radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
Output: false
"""


class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # there are 9 cases in terms of repative pos of a circle and a rectangle
        # case 1-4: the center of the cricle is in 4 corners of the rectangle
        if x_center < x1 and y_center > y2:
            return radius**2 >= (x_center - x1)**2 + (y_center - y2)**2
        elif x_center > x2 and y_center > y2:
            return radius**2 >= (x_center - x2)**2 + (y_center - y2)**2
        elif x_center < x1 and y_center < y1:
            return radius**2 >= (x_center - x1)**2 + (y_center - y1)**2
        elif x_center > x2 and y_center < y1:
            return radius**2 >= (x_center - x2)**2 + (y_center - y1)**2
        
        # case 5-8: the center of the cricle is in 4 sides of the rectangle
        elif x_center < x1:
            return radius >= x1 - x_center
        elif x_center > x2:
            return radius >= x_center - x2
        elif y_center > y2:
            return radius >= y_center - y2
        elif y_center < y1:
            return radius >= y1 - y_center
        
        # case 9: the center of the cricle is in the rectangle
        else:
            return True
