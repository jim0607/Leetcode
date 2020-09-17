"""
1537. Get the Maximum Score

You are given two sorted arrays of distinct integers nums1 and nums2.

A valid path is defined as follows:

Choose array nums1 or nums2 to traverse (from index-0).
Traverse the current array from left to right.
If you are reading any value that is present in nums1 and nums2 you are allowed to change your path to the other array. (Only one repeated value is considered in the valid path).
Score is defined as the sum of uniques values in a valid path.

Return the maximum score you can obtain of all possible valid paths.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
Output: 30
Explanation: Valid paths:
[2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10],  (starting from nums1)
[4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10]    (starting from nums2)
The maximum is obtained with the path in green [2,4,6,8,10].
Example 2:

Input: nums1 = [1,3,5,7,9], nums2 = [3,5,100]
Output: 109
Explanation: Maximum sum is obtained with the path [1,3,5,100].
Example 3:

Input: nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]
Output: 40
Explanation: There are no common elements between nums1 and nums2.
Maximum sum is obtained with the path [6,7,8,9,10].
Example 4:

Input: nums1 = [1,4,5,8,9,11,19], nums2 = [2,3,4,11,12]
Output: 61
"""



"""
Since numbers are strictly increasing, we can always traverse the smaller one using two pointers.
Traversing ([2,4,5,8,10], [4,6,8,10])
will be like [2, 4/4, 5, 6, 8, 10/10]
It two nodes have the same value, we have two choices and pick the larger one, 
then both move nodes one step forward. 
Otherwise, the smaller node moves one step forward.
dp1[i] := max path sum ends with nums1[i-1]
dp2[j] := max path sum ends with nums2[j-1]
"""
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        lens1, lens2 = len(nums1), len(nums2)
        dp1 = [0 for _ in range(lens1 + 1)]     # 这题必须加buffer layer
        dp2 = [0 for _ in range(lens2 + 1)]
        i, j = 1, 1         # 注意从1开始
        while i < lens1 + 1 and j < lens2 + 1:
            if nums1[i-1] == nums2[j-1]:
                dp1[i] = max(dp1[i-1], dp2[j-1]) + nums1[i-1]
                dp2[j] = max(dp1[i-1], dp2[j-1]) + nums2[j-1]
                i += 1
                j += 1
            elif nums1[i-1] < nums2[j-1]:
                dp1[i] = dp1[i-1] + nums1[i-1]
                i += 1
            else:
                dp2[j] = dp2[j-1] + nums2[j-1]
                j += 1
        while i < lens1 + 1:
            dp1[i] = dp1[i-1] + nums1[i-1]
            i += 1
        while j < lens2 + 1:
            dp2[j] = dp2[j-1] + nums2[j-1]
            j += 1

        return max(dp1[-1], dp2[-1]) % (10**9 + 7)
    
"""
topological sort: https://leetcode.com/problems/get-the-maximum-score/discuss/767980/Topological-Sort-O(M-%2B-N)
"""
