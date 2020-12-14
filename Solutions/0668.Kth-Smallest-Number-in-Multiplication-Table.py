"""
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



"""
helper函数定义为是否有k个数大于mid, helper函数利用sorted matrix的特性，可以达到O(m+n).
so overall O((m+n)log(mn))
"""
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        start, end = 1, m*n
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._has_more(m, n, k, mid):    # check if there is more than k numbers less than mid
                end = mid
            else:
                start = mid
        return start if self._has_more(m, n, k, start) else end
    
    def _has_more(self, m, n, k, val):    # check if there is more than k numbers less than mid - O(M+N)
        cnt = 0
        i, j = m, 1     # 从左下角出发
        while i >= 1 and j <= n:
            if i * j <= val:
                cnt += i    # i * j <= val, then j times all numbes on top of i will be less than val 
                j += 1      # 既然这一列都满足了我们去看下一列
            else:
                i -= 1      
        return cnt >= k      # 往左逼近
    
    
"""
heapq solution - O(klogk)
"""
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if k == 1:
            return 1
        if k == m * n:
            return m * n
        
        hq = []
        heappush(hq, (1, 1, 1))
        visited = set()
        visited.add((1, 1))         # 不要忘了visited很重要
        while len(hq) > 0:
            curr_num, curr_i, curr_j = heappop(hq)
            k -= 1
            if k == 0:
                return curr_num
            
            for next_i, next_j in [(curr_i + 1, curr_j), (curr_i, curr_j + 1)]:
                if 1 <= next_i <= m and 1 <= next_j <= n and (next_i, next_j) not in visited:
                    visited.add((next_i, next_j))
                    heappush(hq, (next_i * next_j, next_i, next_j))        
