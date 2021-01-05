"""
949. Largest Time for Given Digits

Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. 
The earliest 24-hour time is 00:00, and the latest is 23:59.

Return the latest 24-hour time in "HH:MM" format.  If no valid time can be made, return an empty string.

Example 1:

Input: A = [1,2,3,4]
Output: "23:41"
Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". 
Of these times, "23:41" is the latest.
Example 2:

Input: A = [5,5,5,5]
Output: ""
Explanation: There are no valid 24-hour times as "55:55" is not valid.
Example 3:

Input: A = [0,0,0,0]
Output: "00:00"
Example 4:

Input: A = [0,0,1,0]
Output: "10:00"
"""



"""
step 1: find all possible permutations - O(4!).
step 2: update max_possible time that can be constructed from the permutations.
"""
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        def backtrack(curr_comb):
            if len(curr_comb) == 4:
                permut.append(curr_comb)
                return
            
            for idx in range(4):
                if idx not in visited:
                    visited.add(idx)
                    backtrack(curr_comb + str(arr[idx]))
                    visited.remove(idx)
                    
        
        permut = []
        visited = set()
        backtrack("")
        
        max_time = -1
        res = ""
        for a, b, c, d in permut:
            hour = int(a) * 10 + int(b)
            minute = int(c) * 10 + int(d)
            if 0 <= hour < 24 and 0 <= minute < 60:
                time = hour * 60 + minute
                if time > max_time:
                    max_time = time
                    res = str(a) + str(b) + ":" + str(c) + str(d)
        return res
