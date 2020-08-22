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
Solution 1: maitain a sorted window.  We can use binary search for remove and insert. 
the overall time complexity is O(nk), because insert takes O(k).
Solution 2: similar with LC 295, we need to maintain two heaps in the window, leftHq and rightHq. 
To slide one step is actually to do two things: step 1. add a number, which is exactly the same as that in LC 295, which is O(logk)
step 2. remove the number that is outside the window; there is not a remove method in heapq, so it takes O(k).
Solution 3: use a SortedList structure, which was implemented using self-balanced tree.  
SortedList enables O(logk) add and remove.  So the total time complexity is O(nlogk) 
"""

from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        odd = k % 2 == 1    # there are odd numbers of items in the window
        
        lst = SortedList()  # maintain a sorted list
        
        
        res = []
        for num in nums[:k]:    # step 1: 把前k个数先放进去
            lst.add(num)
        median = lst[k//2] if odd else (lst[k//2-1] + lst[k//2]) / 2
        res.append(median)
        
        i = k
        while i < len(nums):
            lst.remove(nums[i-k])   # 如果用heapq的话这里是O(k)的, 用sortedList是O(logk)
            lst.add(nums[i])
            median = lst[k//2] if odd else (lst[k//2-1] + lst[k//2]) / 2
            res.append(median)
            i += 1
            
        return res
