"""
1131. Maximum of Absolute Value Expression

Given two arrays of integers with equal lengths, return the maximum value of:

|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

where the maximum is taken over all 0 <= i, j < arr1.length.

Example 1:

Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13
Example 2:

Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
Output: 20
 
Constraints:

2 <= arr1.length == arr2.length <= 40000
-10^6 <= arr1[i], arr2[i] <= 10^6
"""


"""
根据正负符号分为4个situations:
    |arr1[j] - arr1[i]| + |arr2[j] - arr2[i]| + j - i
1.  (arr1[j]  + arr2[j] + j) - (arr1[i]  + arr2[i] + i)
2.  (arr1[j]  - arr2[j] + j) - (arr1[i]  - arr2[i] + i)
3.  (-arr1[j] - arr2[j] + j) - (-arr1[i] - arr2[i] + i)
4.  (-arr1[j] + arr2[j] + j) - (-arr1[i] + arr2[i] + i)
对于每一个situation, 我们用121. Best time to buy stock problem: maintain 一个prev_min
"""
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        res = 0
        
        # situation 1
        arr = [arr1[i] + arr2[i] for i in range(n)]
        curr_min = sys.maxsize
        for i, num in enumerate(arr):
            curr_min = min(curr_min, num + i)
            res = max(res, num + i - curr_min)
        
        # situation 2
        arr = [arr1[i] - arr2[i] for i in range(n)]
        curr_min = sys.maxsize
        for i, num in enumerate(arr):
            curr_min = min(curr_min, num + i)
            res = max(res, num + i - curr_min)
            
        # situation 3
        arr = [-arr1[i] - arr2[i] for i in range(n)]
        curr_min = sys.maxsize
        for i, num in enumerate(arr):
            curr_min = min(curr_min, num + i)
            res = max(res, num + i - curr_min)
            
        # situation 4
        arr = [-arr1[i] + arr2[i] for i in range(n)]
        curr_min = sys.maxsize
        for i, num in enumerate(arr):
            curr_min = min(curr_min, num + i)
            res = max(res, num + i - curr_min)
            
        return res
