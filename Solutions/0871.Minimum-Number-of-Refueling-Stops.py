871. Minimum Number of Refueling Stops

A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  
If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

 

Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can't reach the target (or even the first gas station).
Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: 
We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.



"""
像这种求极值的问题，十有八九要用动态规划 Dynamic Programming 来做，
但是这道题的 dp 定义式并不是直接来定义需要的最少加油站的个数，那样定义的话不太好推导出状态转移方程。
正确的定义应该是根据加油次数能到达的最远距离，我们就用一个一维的 dp 数组，其中 dp[i] 表示加了i次油能到达的最远距离，
dp[i+1] = max(dp[i] + stations[j][1] among all the station that dp[i] can reach) - O(n^2);
return the first i where dp[i] >= target.
"""
"""
dp[i] = the furthest location we can reach if refuled i times.
dp[0] = startFuel
dp[i+1] = max(dp[i]+the station that are within dp[i])
"""
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [0 for _ in range(len(stations)+1)]
        dp[0] = startFuel
        for j, (location, fuel) in enumerate(stations):
            for i in range(j, -1, -1):
                if dp[i] >= location:
                    dp[i+1] = max(dp[i+1], dp[i] + fuel)
        
        for i, loc in enumerate(dp):
            if loc >= target:
                return i
        return -1
        
        
        
"""
在介绍heapq解法之前，我们可以看看不可行的greedy解法，然后在此基础上推出heapq的解法。
"""        
        
"""
solution 2: greedy - O(nlogn). 类似jump game II的想法
sort the stations based on the location; first, see where we can get using the startFuel, say we can get to [10, 40] and [20, 50], 
then we choose the station that can give us the most possible_coverage, 
the left_fuel = last_fuel - (curr_stataion[0]-last_loc) + curr_station[1], 
the next possible_coverage = left_fuel + curr_station[0],
say, we choose [20, 50] and largest next possible_coverge is 75, then we choose the station within 20-75 range, and do the same thing, 
until our next_possible_coverage >= target.
"""
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if target <= startFuel: return 0
        
        stations.sort(key = lambda station: (station[0], station[1]))
        last_coverage = startFuel
        last_fuel = startFuel
        last_loc = 0
        cnt = 0
        i = 0
        while i < len(stations):
            next_coverage = last_coverage
            next_fuel = last_fuel
            next_loc = last_loc
            while i < len(stations) and last_fuel >= stations[i][0] - last_loc:
                if last_fuel + last_loc + stations[i][1] >= next_coverage:
                    next_coverage = last_loc + (last_fuel + stations[i][1])    # next_possible_coverage = 起点+总共有多少油可花
                    next_fuel = last_fuel - (stations[i][0] - last_loc) + stations[i][1]
                    next_loc = stations[i][0]
                i += 1
            
            if next_coverage == last_coverage:
                print("ha", next_coverage, next_loc)
                return -1
            
            last_coverage = next_coverage
            last_fuel = next_fuel
            last_loc = next_loc
            cnt += 1
            
            if next_coverage >= target:
                return cnt
         
        return -1
        
        
"""      
greedy解法看上去很美, 但是过不了case: 150, 50, [[10,20],[15,35],[20,40],[30,60],[50,90]],
因为算法里面没有考虑到很多小步可以凑成一个大步，比如如果每个加油站都停下去加油的话就可以到150了，但是greedy的话只会一步到达[50,90], 而没有选择在中间很多加油站停一下去加油。
那么怎样保证既要贪心地去探寻最大的possible_coverage, 又要保证如果最大的possible_coverage, 就要去探寻次大的possible_coverage呢？
This is when I start to think using a heapq, so that each time we greedily pop the largest possible_coverage, and also store other possible_coverage in the hq,
so that if the leargest_possible_coverage doesn't work, we can still pop our the next largest possible_coverage.
"""


"""
solution 2: heapq - O(nlogn)
heapq stores the fuel at the station. 这题的关键是不要考虑到达的那个station的位置，
我们永远只需要考虑从0出发，中途能加多少油，加的油越多跑得越远. 维护一个possible_coverage变量表示能跑多远.
这个题目用hq的方式跟Dikstra's有点像，都是要贪心地pop出最优解！
"""
from heapq import heappush, heappop

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if target <= startFuel: return 0

        hq = []
        possible_coverage = startFuel
        cnt = 0
        i = 0
        # i < len(stations) is not enough, 要等hq pop完, 
        # 因为hq里面放着油，用完这些油还不能到达target才真正说明到不了target
        while i < len(stations) or hq:  
            while i < len(stations) and possible_coverage >= stations[i][0]:  # 如果可以cover到这个station
                heappush(hq, -stations[i][1])      # 那就把这个station里有油放到hq里面去
                i += 1
                
            if len(hq) > 0:  # 养成好习惯：pop之前check是否为空
                return -1    # 如果hq里面没油了，说明在possible_coverage范围内没油加油站可以供加油
            
            possible_coverage += -heappop(hq)  # 先紧着油多的加油站加油，每加一次油cnt+=1
            cnt += 1
            
            if possible_coverage >= target:
                return cnt
         
        return -1
