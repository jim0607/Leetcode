352. Data Stream as Disjoint Intervals

Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
 

Follow up:

What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?



"""
In addNum method, we just need to append a new interval [val, val] to the intervals - O(1)
In the getIntervals method, we do merge interval just lke 56. Merge intervals - O(NlogN)
"""

import heapq

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []
        
        # Add a seen set to answer the follow up question:
        # What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
        self.seen = set()

    def addNum(self, val: int) -> None:
        if val not in self.seen:
            self.intervals.append([val, val])
            self.seen.add(val)            

    def getIntervals(self) -> List[List[int]]:
        # 下面的就是56. Merge intervals
        self.intervals.sort(key = lambda interval: (interval[0], interval[1]))
        res = []
        for start, end in self.intervals:
            if res and start <= res[-1][-1] + 1:
                res[-1][-1] = max(res[-1][-1], end)
            else:
                res.append([start, end])
                
        self.intervals = res
        return res




"""
也可以用heapq, 是一样的
"""

import heapq

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []
        
        # Add a seen set to answer the follow up question:
        # What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
        self.seen = set()

    def addNum(self, val: int) -> None:
        if val not in self.seen:
            heapq.heappush(self.intervals, [val, val])
            self.seen.add(val)            

    def getIntervals(self) -> List[List[int]]:
        # 下面的就是56. Merge intervals
        res = []
        while self.intervals:
            start, end = heapq.heappop(self.intervals)       # always pop the smallest interval
            if res and start <= res[-1][-1] + 1:
                res[-1][-1] = max(res[-1][-1], end)
            else:
                res.append([start, end])
                
        self.intervals = res
        return res
        
        
        
Follow up:
What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?  

Solution 2: in the addNum method, firstly find the pos of insertion into the intervals, then merge with prev interval and next interval - O(n), 
getIntervals method takes O(1).
This solution is better suit for the follow up question.  Because merge interval only takes O(n), which is better than O(nlogn).  
But remember that in solution 1, the heapq is always almost sorted. so I would say the merge operation is more close to O(n) than O(nlogn).
https://leetcode.com/problems/data-stream-as-disjoint-intervals/discuss/82546/simple-python-solution-with-binary-search
 

 
