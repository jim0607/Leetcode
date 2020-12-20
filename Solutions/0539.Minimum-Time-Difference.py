"""
539. Minimum Time Difference

Given a list of 24-hour clock time points in "HH:MM" format, 
return the minimum minutes difference between any two time-points in the list.

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
"""


class Solution:
    def findMinDifference(self, time_points: List[str]) -> int:
        time_points.sort()
        
        mini_diff = 12*60
        for i in range(1, len(time_points)):
            prev, curr = time_points[i-1].split(":"), time_points[i].split(":")
            prev_hour, prev_min = int(prev[0]), int(prev[1])
            curr_hour, curr_min = int(curr[0]), int(curr[1])
            
            hour_diff = curr_hour - prev_hour
            if hour_diff == 0:
                min_diff = curr_min - prev_min
            else:
                min_diff = (hour_diff - 1) * 60
                min_diff += curr_min + (60 - prev_min)
            mini_diff = min(mini_diff, min_diff)

        # lastly, compare time_points[0] and time_points[-1]  eg:[00:00, 23:59]
        prev, curr = time_points[-1].split(":"), time_points[0].split(":")     
        prev_hour, prev_min = int(prev[0]), int(prev[1])
        curr_hour, curr_min = int(curr[0]), int(curr[1])

        hour_diff = 24 - (prev_hour - curr_hour)
        if hour_diff != 0:
            min_diff = (hour_diff - 1) * 60
            min_diff += curr_min + (60 - prev_min)
            mini_diff = min(mini_diff, min_diff)
        
        return mini_diff
