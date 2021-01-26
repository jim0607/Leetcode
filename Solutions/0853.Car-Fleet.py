"""
853. Car Fleet

N cars are going to the same destination along a one lane road.  The destination is target miles away.

Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.


How many car fleets will arrive at the destination?

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.

Note:

0 <= N <= 10 ^ 4
0 < target <= 10 ^ 6
0 < speed[i] <= 10 ^ 6
0 <= position[i] < target
All initial positions are different.
"""


"""
算法：我的位置比你小，需要的时间还比你少，那说明我可以追上你
这题有一个特点是: 位置靠后的i追上j之后就被j黏住了，不能继续追其他人了
O(NlogN)
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        times = []
        
        for i in range(n):
            pos = position[i]
            spd = speed[i]
            dist = target - pos
            time = dist / spd
            times.append(time)
            
        cars = [(position[i], times[i]) for i in range(n)]
        cars.sort(key=lambda x: (x[0], x[1]))
        times = [time for pos, time in cars]
        
        fleet_cnt = 0
        while len(times) > 0:
            lead_car_arrive_time = times.pop()   # lead_car means lead at the very beginning
            if len(times) == 0:
                return fleet_cnt + 1
            
            if lead_car_arrive_time < times[-1]:  # if the lead_car早早就到了，那他自成一个fleet
                fleet_cnt += 1
            else:
                times[-1] = lead_car_arrive_time  # i追上j之后就被j黏住了
                
        return 0



"""
算法：我的位置比你小，需要的时间还比你少，那说明我可以追上你
O(N^2)
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        times = []
        
        for i in range(n):
            pos = position[i]
            spd = speed[i]
            dist = target - pos
            time = dist / spd
            times.append(time)
            
        cars = [(position[i], times[i]) for i in range(n)]
        cars.sort(key=lambda x: (x[0], x[1]))

        fleet_cnt = n
        for i in range(n - 1):
            for j in range(i + 1, n):
                if cars[i][1] <= cars[j][1]:    # 我的位置比你小，需要的时间还比你少，那说明我可以追上你
                    fleet_cnt -= 1              
                    break       # i追上j之后就被j黏住了，不能再继续追别人了，所以需要break出来
        return fleet_cnt
