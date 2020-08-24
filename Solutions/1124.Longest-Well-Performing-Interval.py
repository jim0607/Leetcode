1124. Longest Well-Performing Interval

We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

Example 1:

Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        nums = []
        for hour in hours:
            if hour > 8:
                nums.append(1)
            else:
                nums.append(-1)
                
        print(nums)
        # now nums is full of 1s and -1s, we need to find the longest subarry that sums > 0
        # what a typical sliding window problem
