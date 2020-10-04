"""
551. Student Attendance Record I

You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
"""



class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt_A = 0
        i = 0
        while i < len(s):
            if s[i] == "A":
                cnt_A += 1
                if cnt_A > 1:
                    return False
            elif s[i] == "L":
                continuous_L = 1
                while i + 1 < len(s) and s[i+1] == "L":
                    continuous_L += 1
                    i += 1
                    if continuous_L > 2:
                        return False
            i += 1
            
        return True
