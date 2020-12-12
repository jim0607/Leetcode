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
        A_cnt = 0
        conL_cnt = 0
        for i in range(len(s)):
            if s[i] == "A":
                A_cnt += 1
                conL_cnt = 0
                if A_cnt > 1:
                    return False
            elif s[i] == "L":
                conL_cnt += 1
                if conL_cnt > 2:
                    return False
            elif s[i] == "P":
                conL_cnt = 0
        return True
