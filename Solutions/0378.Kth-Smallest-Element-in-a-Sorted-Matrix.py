378. Kth Smallest Element in a Sorted Matrix

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.

     
        
"""
利用sorted matrix的性质，从左上角第一个元素开始，添加进heap，然后heap当然自动排序了，然后pop出最小的，然后把最小的那个数的右边和下边的元素分别入heap，这样可以保证每次pop出来的都是最小的。
O(Klog(K) 
"""

from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        hq = []
        added = set()       # store the idx that has already been added into hq
        heappush(hq, (matrix[0][0], (0, 0))) # (i, j) 也要放进hq
        added.add((0, 0))   # 注意这里的visited不能存储matrix[i][j]，因为不同的地方可能存在相同的数
         
        m, n = len(matrix), len(matrix[0])
        res = matrix[0][0]
        for _ in range(k):              # O(klogk)
            res, idx = heappop(hq)
            i, j = idx[0], idx[1]
            if i + 1 < m and (i+1, j) not in added:
                heappush(hq, (matrix[i+1][j], (i+1, j)))
                added.add((i+1, j))
            if j + 1 < n and (i, j+1) not in added:
                heappush(hq, (matrix[i][j+1], (i, j+1)))
                added.add((i, j+1))
        return res

   
"""
soution 2: 传统解法：把每个num都放进hq, 然后heapify, 然后pop k次就是了
"""
from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        hq = []
        added = set()   # store the idx that has already been added into hq
        m, n = len(matrix), len(matrix[0])
        for i in range(m):          # O(n^2)
            for j in range(n):
                heappush(hq, matrix[i][j])
                
        heapify(hq)                 # O(n^2)
        
        res = hq[0]
        for _ in range(k):          # O(2klogN)
            res = heappop(hq)
        return res
   

"""利用heapq，heapq中存储lens - k + 1个数，那还有k-1个数都被pop出来了，最后留在最上面的肯定是第k小的
没有用到sorted matrix的特性，时间复杂度为O(N^2 logM), M = N*2 - K + 1
"""

import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return None

        n = len(matrix)
        m = n * n - k + 1
        heap = []
        for i in range(n):
            for j in range(n):
                heapq.heappush(heap, matrix[i][j])
                if len(heap) > m:
                    heapq.heappop(heap)
        
        return heap[0]
