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
这题可以叫meeting root III. 我们以end pos构造一个heapq, 每次把end pos小于start pos的pop出来
"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # step 1: sort the intervals - interval 题目的第一步！
        trips.sort(key = lambda x: (x[1], x[2]))    
        
        end_hq = []     # a min heapq based on end location
        person = 0      # record how many persons are there on the bus
        for num, start, end in trips:
            # 让这帮乘客上车吧
            heappush(end_hq, (end, start, num))
            person += num
            
            # 让end time < start的乘客都下车
            while len(end_hq) > 0 and start >= end_hq[0][0]:
                person -= heappop(end_hq)[2]
            
            if person > capacity:
                return False
        
        return True
