"""
939. Minimum Area Rectangle

Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
"""


"""
solution 3: O(N^2)
我们choose two diagnol points to iterate - then check if other two diagonal points in p_set. 
"""
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        p_set = set(map(tuple, points))     # 变成set, 这样查找更快

        # 注意我们choose two diagnol points to iterate
        min_area = float("inf")
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:    # diagonal元素必须不能平行于x-axes or y-axes
                    continue
                x3, y3 = x2, y1
                x4, y4 = x1, y2
                if (x3, y3) in p_set and (x4, y4) in p_set:
                    min_area = min(min_area, abs(x1 - x2) * abs(y1 - y2))

        return 0 if min_area == float("inf") else min_area

        

"""
solution 2: O(N^2logN)
use a hashmap to store diagnals: (lens, x_ctr, y_ctr) --> (slope)
"""
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[0], x[1]))
        
        mapping = collections.defaultdict(list)  # (lens, x_ctr, y_ctr) --> (slope)
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:
                    continue
                x_ctr, y_ctr = (x1 + x2) / 2, (y1 + y2) / 2
                lens = (x1 - x2)**2 + (y1 - y2)**2
                slope = (y1 - y2) / (x1 - x2)
                mapping[(lens, x_ctr, y_ctr)].append(slope)
        min_area = float("inf")
        for (lens, x_ctr, y_ctr), slopes in mapping.items():
            if len(slopes) >= 2:
                min_area = min(min_area, self._find_min_area(lens, slopes))
        return 0 if min_area == float("inf") else round(min_area)
    
    def _find_min_area(self, lens, slopes):
        """
        algorithm: 长和宽相差越大，面积越小
        """
        slopes.sort()           # this takes O(NlogN)
        left, right = 0, len(slopes) - 1
        while left < right:
            if slopes[left] + slopes[right] < 0:
                left += 1
            elif slopes[left] + slopes[right] > 0:
                right -= 1
            else:
                k = slopes[right]
                return lens * k / (1 + k**2)
        return float("inf")
        



"""
solution 1: O(N^3)
step 1: sort the points.
step 2: buiid a hashmap to store (key: start_x, val: end_x that is parellel to x_axis);
build another hashmap to store (key: start_y, val: end_y that is parellel to y_axis).
step 3: traversal the points and check each (x, y) as bottom-left corner as starting point.
"""
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[0], x[1]))

        x_map = collections.defaultdict(set)
        y_map = collections.defaultdict(set)
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                if points[j][1] == points[i][1]:
                    x_map[tuple(points[i])].add(tuple(points[j]))
                if points[j][0] == points[i][0]:
                    y_map[tuple(points[i])].add(tuple(points[j]))

        min_area = float("inf")
        for x, y in points:
            frst_p = (x, y)
            for secd_p in x_map[frst_p]:
                for thrd_p in y_map[frst_p]:
                    if y_map[secd_p] & x_map[thrd_p]:
                        x_lens = secd_p[0] - x
                        y_lens = thrd_p[1] - y
                        min_area = min(min_area, x_lens * y_lens)
        return 0 if min_area == float("inf") else min_area
