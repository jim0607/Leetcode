149. Max Points on a Line

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6



"""
y = kx + b, points on a line share the same slope k and same intercept b.
So we can use a dictionary to store the (k, b) as key and points pos as value.
"""
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        if len(points) <= 2:
            return len(points)
        
        dic = collections.defaultdict(set)
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points):
                if i == j:
                    continue
                if x1 == x2:
                    continue
                k = (y2 - y1) / (x2 - x1)       # 这里做除法可能会导致99999998/99999999 = 99999997/999999999, 所以导致错误，方法是转换成乘法
                b = (y1 * x2 - y2 * x1) / (x2 - x1)
                dic[(k, b)].add((x1, y1, i))
                dic[(k, b)].add((x2, y2, j))
                
        dic_inf = collections.defaultdict(set)
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points):
                if i == j:
                    continue
                if x1 == x2:
                    dic_inf[x1].add((x1, y1, i))
                    dic_inf[x1].add((x2, y2, j))

        max_point = 2
        if dic:
            max_point = max(len(lst) for lst in dic.values())
        if dic_inf:
            max_point = max(max_point, max(len(lst) for lst in dic_inf.values()))
        
        return max_point
