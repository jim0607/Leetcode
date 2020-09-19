"""
436. Find Right Interval

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:

You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
 

Example 1:

Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
 

Example 2:

Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
 

Example 3:

Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.
"""


"""
step 1: include the idx information into the interval;
step 2: then sort the intervals based on start time;
step 3: scan the interval and update res, using binary search.
"""
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        info = []
        for i, (start, end) in enumerate(intervals):
            info.append((start, end, i))
        
        info.sort(key = lambda x: x[0])
        
        res = [-1 for _ in range(len(intervals))]
        for start, end, i in info:
            res[i] = self._binary_search(info, end)
        return res
    
    def _binary_search(self, info, target):
        """
        Return the idx of the first start that larger than target
        """
        left, right = 0, len(info) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if info[mid][0] >= target:  # 往左逼to find the first start that larger than target
                right = mid
            else:
                left = mid
        if info[left][0] >= target:
            return info[left][2] 
        if info[right][0] >= target:
            return info[right][2]
        return -1
