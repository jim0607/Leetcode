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
Sort events. use a min hq stores the end time of events cuz we want to pop the min end time first.
loop over the curr_time from 1 to max day 100000, each day, we do:
1. add new events that start before curr_time to hq so that we can attend the event; 
2. remove the events that are already ended before curr_time; 
3. greedily attend the event that ends soonest by popping from the hq, and update cnt += 1.
"""
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: (x[0], x[1]))
        
        cnt = 0
        hq = []     # min heapq to store the the end time
        min_day = min(event[0] for event in events)
        max_day = max(event[1] for event in events)
        event_idx = 0
        for curr_day in range(min_day, max_day + 1):
            # 1. add new events that start before curr_time to hq so that we can attend the event
            while event_idx < len(events) and events[event_idx][0] <= curr_day:
                heappush(hq, events[event_idx][1])
                event_idx += 1
                
            # 2. remove the events that are already ended before curr_time
            while len(hq) > 0 and hq[0] < curr_day:
                heappop(hq)
                
            # greedily attend the event that ends soonest by popping from the hq, and update cnt += 1
            if len(hq) > 0:
                heappop(hq)
                cnt += 1
            
        return cnt 
