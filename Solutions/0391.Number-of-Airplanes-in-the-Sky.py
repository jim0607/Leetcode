391. Number of Airplanes in the Sky

Given an list interval, which are taking off and landing time of the flight. 
How many airplanes are there at most at the same time in the sky?

Example
Example 1:

Input: [(1, 10), (2, 3), (5, 8), (4, 7)]
Output: 3
Explanation:
The first airplane takes off at 1 and lands at 10.
The second ariplane takes off at 2 and lands at 3.
The third ariplane takes off at 5 and lands at 8.
The forth ariplane takes off at 4 and lands at 7.
During 5 to 6, there are three airplanes in the sky.
Example 2:

Input: [(1, 2), (2, 3), (3, 4)]
Output: 1
Explanation: Landing happen before taking off.
Notice
If landing and taking off of different planes happen at the same time, we consider landing should happen at first.



"""
扫描线做法：
碰到interval的start，也就是起飞一架飞机，当前天上的飞机数++。
碰到interval的end，也就是降落一架飞机，当前天上的飞机数--。
我们分别把所有的start和所有的end放进两个数组，并排序。
然后从第一个start开始统计，碰到start就加一，碰到end就减一。并且同时维护一个最大飞机数的max。
当所有的start统计过以后，我们就有答案了。后面的end只会往下减，所以不用再看了。
"""
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        departure, arrival = [], []
        for airplane in airplanes:
            departure.append(airplane.start)
            arrival.append(airplane.end)
        
        departure.sort()       # O(NlogN)
        arrival.sort()
        
        currAirplane, maxAirplane = 0, 0
        i, j = 0, 0
        while i < len(departure) and j < len(arrival):
            if departure[i] < arrival[j]:
                currAirplane += 1
                i += 1
            elif departure[i] > arrival[j]:
                currAirplane -= 1
                j += 1
            else:
                i += 1
                j += 1
                
            maxAirplane = max(maxAirplane, currAirplane)
        
        return maxAirplane
