"""
1094. Car Pooling

You are driving a vehicle that has capacity empty seats initially available for passengers.  
The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: 
the number of passengers that must be picked up, and the locations to pick them up and drop them off.  
The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

 
Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
"""


"""
这题可以叫meeting root III. 我们以end pos构造一个heapq, 每次把end pos小于start pos的pop出来
"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: (x[1], x[2], x[0]))
        
        end_hq = []     # a min heapq based on end location
        curr_cnt = 0    # record how many persons are there on the bus
        for cnt, start, end in trips:
            # 让这帮乘客上车吧
            heappush(end_hq, (end, cnt))
            curr_cnt += cnt
            
            # 让end time < start的乘客都下车
            while len(end_hq) > 0 and end_hq[0][0] <= start:
                curr_cnt -= heappop(end_hq)[1]
                
            if curr_cnt > capacity:
                return False
            
        return True
