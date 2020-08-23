1229. Meeting Scheduler

Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.  

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

 

Example 1:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]
Example 2:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []


 """
to find the overlap of two intervals. We loop over the two intervals. 
一个interval与另一个interval的位置关系就三种情况(1. 没有交集; 2. 一个包含了另一个; 3. 有交集但是没有谁能完全包含谁)
"""
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        res = []
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            start1, end1 = slots1[i][0], slots1[i][1]
            start2, end2 = slots2[j][0], slots2[j][1]
            
            # case 1: 两个interval不相交
            if start1 > end2:
                j += 1
            elif start2 > end1:
                i += 1
            
            # case 2: 一个interval包含另一个
            elif start1 <= start2 and end1 >= end2:
                res = [start2, end2]
                j += 1
            elif start2 <= start1 and end2 >= end1:
                res = [start1, end1]
                i += 1
                
            # case 3: 相交但并不包含
            elif start2 <= end1 <= end2:
                res = [start2, end1]
                i += 1
            elif start1 <= end2 <= end1:
                res = [start1, end2]
                j += 1
                
            if len(res) > 0 and res[1] - res[0] >= duration:
                return [res[0], res[0]+duration]
            
        return []
 
 
"""
solution 2: 代码更短但是逻辑没那么清楚
"""
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            start1, end1 = slots1[i][0], slots1[i][1]
            start2, end2 = slots2[j][0], slots2[j][1]
            
            if min(end1, end2) - max(start1, start2) >= duration:
                return [max(start1, start2), max(start1, start2) + duration]
            
            if end2 > end1:
                i += 1
            else:
                j += 1
                
        return []
