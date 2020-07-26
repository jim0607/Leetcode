349. Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]


"""
Intersection不要求是连续的，所以直接output公共的元素就行
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)
        
        
"""
This is a Facebook interview question.
They ask for the intersection, which has a trivial solution using a hash or a set.

Then they ask you to solve it under these constraints:
O(n) time and O(1) space (the resulting array of intersections is not taken into consideration) if the lists are sorted.

Below I wrote down my solution for the Facebook follow up question - O(m+n), O(1) assuming the lists are sorted
"""
"""
This is a Facebook interview question.
They ask for the intersection, which has a trivial solution using a hash or a set.

Then they ask you to solve it under these constraints:
O(n) time and O(1) space (the resulting array of intersections is not taken into consideration) if the lists are sorted.

Cases to take into consideration include:
duplicates, negative values, single value lists, 0's, and empty list arguments.
Other considerations might include sparse arrays.
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()    # assume nums are sorted
        nums2.sort()
        i, j = 0, 0
        lens1, lens2 = len(nums1), len(nums2)
        res = []
        while i < lens1 and j < lens2:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                while i + 1 < lens1 and nums1[i] == nums1[i+1]:     # 必须掌握的去重方法
                    i += 1
                while j + 1 < lens2 and nums2[j] == nums2[j + 1]:
                    j += 1
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res
 
