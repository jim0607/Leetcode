218. The Skyline Problem

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

Buildings Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]


    
"""
不难发现这些关键点的特征是：竖直线上轮廓升高或者降低的终点,
所以核心思路是：从左至右遍历建筑物，记录当前的最高轮廓，如果产生变化则记录一个关键点       
"""
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 首先记录构造一个建筑物的两种关键事件
        # 第一种是轮廓升高事件(L, -H)、第二种是轮廓降低事件(R, 0)
        # 轮廓升高事件(L, -H, R)中的R用于后面的最小堆
        events = [(left, height, right) for left, right, height in buildings]
        events += [(right, 0, 0) for _, right, _ in buildings]
        
        # 先根据L从小到大排序、再根据H从大到小排序
        # 这是因为我们要维护一个堆保存当前最高的轮廓
        events.sort(key = lambda x: (x[0], -x[1], x[2]))
        
        hq = [(0, float("inf"))]  # 保存当前最高的轮廓(-H, R)
        
        res = [[0, 0]]
        for left, height, right in events:
            # 如果是轮廓升高事件则记录到最大堆中
            if height != 0:
                heappush(hq, (-height, right))
            
            # 根据当前遍历的位置L，判断最高轮廓是否有效，无效则剔除
            # pop buildings that end before curPos, cuz they are no longer "alive"
            while hq[0][1] <= left:
                heappop(hq)
                
            # 如果当前的最高轮廓发生了变化，则记录一个关键点
            if res[-1][1] != -hq[0][0]:
                res.append([left, -hq[0][0]])
                
        return res[1:]
    
    

"""https://leetcode.com/problems/the-skyline-problem/discuss/61210/14-line-python-code-straightforward-and-easy-to-understand"""
from heapq import *
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:                
        lens = len(buildings)
        
        # possible corner positions
        positions = []
        for left, right, height in buildings:
            positions.append(left)
            positions.append(right)
            
        positions.sort()    # 扫描线问题一般都需要提前sort好数组
            
        alive = []      # a maxHeap to store all alive buildings, 存高度和终点
        res = []        # res 里面需要保存的其实是每一次高度发生变化时的终点
        prevHeight = 0
        i = 0
        for currPos in positions:
            # pop buildings that end before curPos, cuz they are no longer "alive"
            # It's also worth noting that when we remove buildings that are no longer alive,
            # there is no need to remove all "dead" buildings, 
            # as long as they are low enough and wouldn't stop us from finding the highest alive building. 
            # For instance, if the input is [ [1, 4, 20], [2, 3, 10] ], when we reach x = 3, 
            # the building of height 10 is still in the heapq, but it doesn't matter.
            # so we only remove the buldings that are very tall (on the top of maxHeap)
            # that's why we use .pop instead of .remove in 山景城一姐的video
            while alive and alive[0][1] <= currPos:
                heappop(alive)
                
            # push [negative_height, end_point] of all buildings that start before curPos
            # cuz they are candidates for the current highest building
            while i < lens and buildings[i][0] <= currPos:
                heappush(alive, (-buildings[i][2], buildings[i][1]))   # maitain a maxHeap for alive buildings
                i += 1
                  
            # now alive[0] is the largest height at the current position
            if alive:
                currHeight = -alive[0][0]
                if currHeight != prevHeight:    # 说明出现了一个拐点要么上升要么下降，这时候就需要append拐点了
                    res.append([currPos, currHeight])
                    prevHeight = currHeight
            else:       # no building, horizontal line
                res.append([currPos, 0])
                
        # 简单给res去个重, anchor keep all the non-duplicate on it's left
        anchor, curr = 0, 1
        for curr in range(len(res)):
            if res[curr] != res[anchor]:
                anchor += 1
                res[anchor], res[curr] = res[curr], res[anchor]
                
        return res[:anchor+1]
