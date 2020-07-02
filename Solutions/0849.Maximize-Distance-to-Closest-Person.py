849. Maximize Distance to Closest Person

In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.



"""
遍历过程中不断update idx_of_1和max_dist就可以了，把seats[0]==0和seats[-1]==0单独拿出来判断。
讨论：这道题的一个很好的 follow up 是让我们返回爱丽丝坐下的位置.
那么要在结果 res 可以被更新的时候，同时还应该记录下连续空位的起始位置 start，这样有了 start 和 最大距离 res，那么就可以定位出爱丽丝的座位了。
"""
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist = 0
        idx_of_1 = -1
        for i, seat in enumerate(seats):
            if seat == 1:
                if idx_of_1 != -1:
                    max_dist = max((i - idx_of_1) // 2, max_dist) 
                idx_of_1 = i
                
        if seats[0] == 0:
            i = 0
            while i < len(seats):
                if seats[i] != 1:
                    i += 1
                else:
                    break
            max_dist = max(max_dist, i)
            
        if seats[-1] == 0:
            i = len(seats) - 1
            while i >= 0:
                if seats[i] != 1:
                    i -= 1
                else:
                    break
            max_dist = max(max_dist, len(seats) - 1 - i)
            
        return max_dist
