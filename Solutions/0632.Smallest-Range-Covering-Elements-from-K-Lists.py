632. Smallest Range Covering Elements from K Lists

You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:

Input: [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].



"""
heapq solution: O(m+nlogm) where m is len(nums), n is len(lst)
hq stores (the item in the lst, the lst_idx of where lst is in the nums, the num_idx where the num is in the lst)
whenver a min_val is popped, we compare the max_val-min_val with the previous diff. 
Then we push (nums[lst_idx][num_idx+1], lst_idx, num_idx+1) into the heapq and update max_val in the heapq
"""

from heapq import *

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        hq = []
        for lst_idx, lst in enumerate(nums):
            hq.append((lst[0], lst_idx, 0))   # hq stores (the item in the lst, the lst_idx of where lst is in the nums, the num_idx where the num is in the lst)
            
        heapq.heapify(hq)   # O(m) where m is len(nums)
        
        max_val = max(lst[0] for lst in nums)
        res = -float("inf"), float("inf")
        while hq:
            min_val, lst_idx, num_idx = heappop(hq)
            if max_val - min_val < res[1] - res[0]:
                res = min_val, max_val
            if num_idx == len(nums[lst_idx]) - 1:    # meaning that cannot append another val from this lst anymore
                return res
            
            heappush(hq, (nums[lst_idx][num_idx+1], lst_idx, num_idx+1))
            max_val = max(max_val, nums[lst_idx][num_idx+1])
