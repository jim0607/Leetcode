"""
480. Sliding Window Median

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].
"""

"""
Solution 1:
maitain a sorted window. We can use binary search for remove and insert.
Because insert takes O(k), the overall time complexity is O(nk).

Solution 2:
similar with LC 295, we need to maintain two heaps in the window, leftHq and rightHq.
To slide one step is actually to do two things: step 1. add a number, which is exactly the same as that in LC 295, which is O(logk)
step 2. remove the number that is outside the window; there is not a remove method in heapq, so it takes O(k). So overall the heapq solution will take O(nk).

Solution 3:
use a SortedList structure, which was implemented using self-balanced tree.
SortedList enables O(logk) add and O(logk) remove. So the total time complexity is O(nlogk).
"""

from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lst = SortedList()              # maintain a sorted list
        res = []
        for i in range(len(nums)):
            lst.add(nums[i])            # O(logk)
            if i >= k:
                lst.remove(nums[i-k])   # if we use heapq here, it takes O(k) here, but for sortedList, it takes O(logk)
            if i >= k - 1:
                median = lst[k//2] if k % 2 == 1 else (lst[k//2] + lst[k//2-1]) / 2
                res.append(median)
        return res
