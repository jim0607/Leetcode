"""
1232. Check If It Is a Straight Line

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
Check if these points make a straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
"""


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        if x1 == x2:
            for x, y in coordinates:
                if x != x1:
                    return False       
        else:
            slope = (y2 - y1) / (x2 - x1)
            intercept = (x2*y1 - x1*y2) / (x2 - x1)
            for x, y in coordinates:
                expected_y = slope * x + intercept
                if y != expected_y:
                    return False                
        return True
