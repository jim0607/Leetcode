253. Meeting Rooms II

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2


    
"""
minimum meeting rooms required could be understood us maximum meeting rooms in use
Then this problem is exaclty the same as the lintcode 0391. Number of Airplanes in the Sky
Sweep line: 
扫描线做法：碰到interval的start，也就是起飞一架飞机，当前天上的飞机数++。碰到interval的end，也就是降落一架飞机，当前天上的飞机数--。
Step 1: 我们分别把所有的start和所有的end放进两个数组，并排序。Step 2: 然后从第一个start开始统计，碰到start较小就加一，碰到end较小就减一。并且同时维护一个最大飞机数的max。
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
            
        start.sort()
        end.sort()
            
        curr_in_use, max_in_use = 0, 0
        i, j = 0, 0
        while i < len(start) and j < len(end):
            if start[i] < end[j]:
                curr_in_use += 1
                i += 1
            else:
                curr_in_use -= 1
                j += 1
                
            max_in_use = max(max_in_use, curr_in_use)
            
        return max_in_use
                  
    
 
Solutoin 2: heapq
"""
put an interval into heap, if the end of the interval is less then the min-end of the heap, then cnt += 1, else just push in and pop the min end
O(NlogN), O(N)"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: (x[0], x[1]))     # need to sort first
        
        heap = []
        cnt = 0
        for start, end in intervals:
            heapq.heappush(heap, [end, start])      # 构造一个以end排序的最小堆
            if start < heap[0][0]:      # 如果start小于最小的end，那就需要重开一个会议室
                cnt += 1
            else:
                heapq.heappop(heap)     # 如果start大于最小的end, 那就可以共用一个meeting room了，
                                        # 此时这个meeting room的心得end time就不是heap[0][0]了，所以要pop出来
                                        # 为了保证不要误pop了，eg: [1, 2]遇到[1000,1001], 如果把[1,2] pop 出来太可惜了，后面可能还有[3,5],[20,30]等等都可以fit in the smae meeting room
                                        # 这就是为什么要做intervals.sort()的原因
        return cnt
