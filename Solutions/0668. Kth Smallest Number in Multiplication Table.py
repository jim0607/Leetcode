668. Kth Smallest Number in Multiplication Table

Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?

Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.

Example 1:
Input: m = 3, n = 3, k = 5
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6
3	6	9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).
Example 2:
Input: m = 2, n = 3, k = 6
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
Note:
The m and n will be in the range [1, 30000].
The k will be in the range [1, m * n]

"""
helper函数定义为是否有k个数大于mid, helper函数利用sorted matrix的特性，可以达到O(m+n).
so overall O((m+n)log(mn))
"""
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        start, end = 1, m*n
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._has_more(m, n, k, mid):      # check if there is more than k numbers less than mid
                end = mid
            else:
                start = mid
        return end if self._has_more(m, n, k, end) else start
    
    def _has_more(self, m, n, k, val):
        i, j = 1, n
        cnt = 0
        while i <= m and j >= 1:
            if i * j <= val:   # i代表行，j代表列
                cnt += j       # i * j <= val, then i times all numbes before j will be less than val     
                i += 1         # 既然这一行都满足了，咱们去下一行看
            else:
                j -= 1
        return cnt >= k
