"""
1213. Intersection of Three Sorted Arrays

Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
"""


"""
solution 1: use a freq dictionary: the elements that appeared in all the arrays would have a frequency of 3.
solution 2: three pointers since the arrs are sorted.
solution 3: find intersection inter of arr1 and arr2 first, then find the intersection of inter with arr3.
"""
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        i, j, k = 0, 0, 0
        res = []
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            min_num = min(arr1[i], arr2[j], arr3[k])
            if arr1[i] == arr2[j] == arr3[k]:
                res.append(arr1[i])
                i += 1
                j += 1
                k += 1
            elif arr1[i] == min_num:
                i += 1
            elif arr2[j] == min_num:
                j += 1
            elif arr3[k] == min_num:
                k += 1
        return res
