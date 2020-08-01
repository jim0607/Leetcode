1094. Car Pooling

You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

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
这题可以叫meeting root III. 我们以end pos构造一个heapq, 每次把end pos小于start pos的pop出来
"""
from heapq import heappush, heappop

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda trip: (trip[1], trip[2]))   # step 1: sort the intervals

        end_pos = []        # 以end pos构造一个heapq
        person = 0          # record how many persons are there on the bus
        for num, start, end in trips:
            heappush(end_pos, (end, start, num))
            
            while start >= end_pos[0][0]:   # 只要是end < start, 说明那些人早就到了，让他们下车
                person -= heappop(end_pos)[2]       
                
            person += num           # 别忘了新的一拨人要上车 
            
            if person > capacity:
                return False
            
        return True
