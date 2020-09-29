"""
391. Perfect Rectangle

Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. 
(coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).
"""



"""
In order to form a perfect rectangle, two condictions must be satisfied:
condition 1. for all the coordinates, there are 4 and only 4 coordinates that appear only once, others appear either twice or 4 times.  
So we can use a set to store all the coordinates and cnt their appear times
condition 2. the sum of area of all the small rectangles should be the same as the whole big one 
(the area enclosed by the 4 coordinates in condition 1)
"""
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        coordinates = set()
        area = 0
        for rec in rectangles:
            bottom_left = (rec[0], rec[1])
            bottom_right = (rec[0], rec[3])
            top_left = (rec[2], rec[1])
            top_right = (rec[2], rec[3])
            
            area += (rec[2] - rec[0]) * (rec[3] - rec[1])
            
            for coordinate in [bottom_left, bottom_right, top_left, top_right]:
                if coordinate not in coordinates:
                    coordinates.add(coordinate)
                else:
                    coordinates.remove(coordinate)
        
        if len(coordinates) != 4:   # condition 1
            return False        # 注意光满足condition 1还不够 - eg: [[1,1,2,2],[1,1,2,2],[2,1,3,2]]

        bottom_left = sorted(coordinates)[0]    # here we used sorted for set, but there are only 4 elements in the set, so O(1)
        top_right = sorted(coordinates)[3]
        return area == (top_right[0] - bottom_left[0]) * (top_right[1] - bottom_left[1])    # condition 2
