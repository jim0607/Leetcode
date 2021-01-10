"""
1287. Element Appearing More Than 25% In Sorted Array

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
"""


"""
想想如果我们需要求sorted arr 里 more than n//2 times的num, 只需要直接return arr[n//2]就可以了
同理我们可以求more than 25%的num.
step 1: 找出 n//4, 2n//4, 3n//4 位置处的num, 因为答案只可能存在于这三个位置上
step 2: 对这三个num分别做binary search求出first_pos and last_pos, 如果last_pos - first_pos >= n//4 就找到了
"""
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        num1 = arr[n//4]
        num2 = arr[n//2]
        num3 = arr[3*n//4]
        first1 = self.binary_search_first(arr, num1)
        last1 = self.binary_search_last(arr, num1)
        if last1 - first1 >= n // 4:
            return num1
        first2 = self.binary_search_first(arr, num2)
        last2 = self.binary_search_last(arr, num2)
        if last2 - first2 >= n // 4:
            return num2
        return num3
    
    def binary_search_first(self, arr, num):
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid] >= num:
                end = mid
            else:
                start = mid
        return start if arr[start] == num else end
    
    def binary_search_last(self, arr, num):
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid] > num:
                end = mid
            else:
                start = mid
        return end if arr[end] == num else start
