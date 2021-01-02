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
        for i, ch in enumerate(s):
            if ch == "A":
                A_cnt += 1
                if A_cnt > 1:
                    return False
            elif ch == "L":
                if i + 2 < len(s) and s[i:i+3] == "LLL":
                    return False
        return True
