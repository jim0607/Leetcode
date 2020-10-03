"""
963. Minimum Area Rectangle II

Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the x and y axes.

If there isn't any rectangle, return 0.

Example 1:

Input: [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
Example 2:

Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output: 1.00000
Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
Example 3:

Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output: 0
Explanation: There is no possible rectangle to form from these points.
Example 4:


Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.
"""



"""
如果两条对角线相等，且平分对方，则这两条.
use a hashmap to map (对角线的长度, 对角线的中点坐标) to a list of (对角线连接的两点的坐标)
"""
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        # step 1: construct the hashmap
        mapping = collections.defaultdict(list)
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                diagnal_mid = ((x2 + x1) / 2, (y2 + y1) / 2)
                diagnal_len = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
                mapping[(diagnal_len, diagnal_mid)].append((x1, y1, x2, y2))
        
        # step 2: calculate and compare each possible rectangle
        min_area = float("inf")
        for pairs in mapping.values():
            if len(pairs) <= 1:
                continue
            for i in range(len(pairs) - 1):
                for j in range(i + 1, len(pairs)):
                    x1, y1, x2, y2 = pairs[i]
                    x3, y3, x4, y4 = pairs[j]
                    edge_1 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
                    edge_2 = math.sqrt((x1 - x4)**2 + (y1 - y4)**2)
                    area = edge_1 * edge_2
                    min_area = min(min_area, area)
        return 0 if min_area == float("inf") else min_area
