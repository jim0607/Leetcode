"""
356. Line Reflection

Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points symmetrically, 
in other words, answer whether or not if there exists a line that after reflecting all points over the 
given line the set of the original points is the same that the reflected ones.

Note that there can be repeated points.


Example 1:

Input: points = [[1,1],[-1,1]]
Output: true
Explanation: We can choose the line x = 0.

Example 2:
Input: points = [[1,1],[-1,-1]]
Output: false
Explanation: We can't choose a line.
"""


"""
use a hashset to store all the points. loop through the points and check if (max_x + min_x - x, y)  in hashset
"""
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        n = len(points)
        if n <= 1:
            return True
        
        min_x = min(point[0] for point in points)
        max_x = max(point[0] for point in points)
        
        hashset = set(tuple(point) for point in points)   # store the points for fast look up
        
        for x, y in points:
            if (max_x + min_x - x, y) not in hashset:
                return False
            
        return True
