1353. Maximum Number of Events That Can Be Attended

Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. Notice that you can only attend one event at any time d.

Return the maximum number of events you can attend.


Example 1:


Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
Example 3:

Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output: 4
Example 4:

Input: events = [[1,100000]]
Output: 1
Example 5:

Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
Output: 7


"""
Sort events. Priority queue pq keeps the current open events.
Iterate from the day 1 to day 100000, each day, we 1. add new events starting on day d to the queue pq; 
2. remove the events that are already closed; 
3. greedily attend the event that ends soonest, if we can attend a meeting, we increment the res.
"""
from heapq import heappush, heappop

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda event: (event[0], event[1]))
        
        hq = []     # hq stores the event end time that are avaliable to attend
        cnt = 0
        event_idx = 0
        day = min(event[0] for event in events)
        total_days = max(event[1] for event in events)
        
        while day <= total_days:
            # step 1: add those events that are candidates to attend
            while event_idx < len(events) and events[event_idx][0] <= day:
                heappush(hq, events[event_idx][1])
                event_idx += 1
            
            # step 2: remove those events that already outdated
            while hq and hq[0] < day:
                heappop(hq)
                
            # step 3: attend the events that ended earliest - Greedy
            if hq:
                heappop(hq)
                cnt += 1
                
            day += 1
                
        return cnt
