"""
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



"""
step 1: check what is the distace if he sits at two ends;
step 2: check what is the distance if he sits in the middle, two pinters: same method as 245. Shortest Word Distance III
"""
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # step 1: check what is the distace if he sits at two ends
        start, end = 0, len(seats) - 1
        for i, seat in enumerate(seats):
            if seat == 1:
                start = i
                break
        for j in range(len(seats) - 1, -1 ,-1):
            if seats[j] == 1:
                end = j
                break
        max_dist = max(start, len(seats) - 1 - end)
        
        # step 2: check what is the distance if he sits in the middle
        # two pinters: same method as 245. Shortest Word Distance III 
        prev, curr = start, start
        for i in range(start, end + 1):
            if seats[i] == 1:
                prev = curr
                curr = i
                max_dist = max(max_dist, (curr - prev) // 2)
                
        return max_dist
