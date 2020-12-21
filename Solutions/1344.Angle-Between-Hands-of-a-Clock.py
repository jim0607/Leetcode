"""
1344. Angle Between Hands of a Clock

Given two numbers, hour and minutes. 
Return the smaller angle (in degrees) formed between the hour and the minute hand.

Example 1:

Input: hour = 12, minutes = 30
Output: 165
Example 2:

Input: hour = 3, minutes = 30
Output: 75
Example 3:

Input: hour = 3, minutes = 15
Output: 7.5
Example 4:

Input: hour = 4, minutes = 50
Output: 155
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_ratio = 360 / 12
        min_ratio = 360 / 60
        min_angle = min_ratio * minutes
        hour %= 12
        hour_angle = hour_ratio * hour + 360 / 60 / 12 * minutes
        angle = abs(hour_angle - min_angle)
        angle = min(angle, abs(360 - hour_angle + min_angle), abs(360 + hour_angle - min_angle))
        return angle
