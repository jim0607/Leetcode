"""
1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

Given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with sum equal target. 
There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.


Example 1:

Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
Example 2:

Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.
Example 3:

Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.
Example 4:

Input: arr = [5,5,4,4,5], target = 3
Output: -1
Explanation: We cannot find a sub-array of sum = 3.
Example 5:

Input: arr = [3,1,1,1,5,1,2,1], target = 3
Output: 3
Explanation: Note that sub-arrays [1,2] and [2,1] cannot be an answer because they overlap.
 
Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 1000
1 <= target <= 10^8
"""




"""
step 1: construct a pre_sum and a suf_sum.
Step 2: then use the pre_sum and suf_sum to construct two lists:
pre_min[i] = minimum lens of valid subarray that ends before i.
suf_min[i] = minimum lens of valid subarray that starts after i.
step 3: find the ans as we iterate the arr
"""
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # step 1: construct pre_sum and suf_sum
        n = len(arr)
        pre_sum = [0 for _ in range(n + 1)]
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + arr[i]
            
        suf_sum = [0 for _ in range(n + 1)]
        for j in range(n-1, -1, -1):
            suf_sum[j] = suf_sum[j+1] + arr[j]
            
        # step 2: construct pre_min and suf_min
        # 我们可以用sliding window因为题目给的是positive numbers, 如果有negative numbers那就用一个hashmpa记录pre_sum --> idx
        pre_min = [float("inf") for _ in range(n + 1)]
        i = 0
        for j in range(1, n + 1):
            while i < j and pre_sum[j] - pre_sum[i] > target:
                i += 1
            if pre_sum[j] - pre_sum[i] == target:
                pre_min[j] = min(pre_min[j-1], j - i)   # 注意这里dp的更新
            else:
                pre_min[j] = pre_min[j-1]

        suf_min = [float("inf") for _ in range(n + 1)]
        j = n
        for i in range(n-1, -1, -1):
            while j > i and suf_sum[i] - suf_sum[j] > target:
                j -= 1
            if suf_sum[i] - suf_sum[j] == target:
                suf_min[i] = min(suf_min[i+1], j - i)
            else:
                suf_min[i] = suf_min[i+1]

        # step 3: find the ans as we iterate the arr
        res = float("inf")
        for i in range(n + 1):
            res = min(res, pre_min[i] + suf_min[i])
            
        return -1 if res == float("inf") else res
