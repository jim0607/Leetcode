253. Meeting Rooms II

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2


"""
put an interval into heap, if the end of the interval is less then the min-end of the heap, then cnt += 1, else just push in and pop the min end
O(NlogN), O(N)"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        heap = []
        cnt = 0
        for start, end in intervals:
            heapq.heappush(heap, [end, start])      # 构造一个以end排序的最小堆
            if start < heap[0][0]:      # 如果start小于最小的end，那就需要重开一个会议室
                cnt += 1
            else:
                heapq.heappop(heap)
                
        return cnt
