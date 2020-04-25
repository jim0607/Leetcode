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
