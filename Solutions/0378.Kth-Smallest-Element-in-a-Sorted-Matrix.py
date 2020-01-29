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
        
        
"""
利用sorted matrix的性质，从左上角第一个元素开始，添加进heap，然后heap当然自动排序了，然后pop出最小的，然后把最小的那个数的右边和下边的元素分别入heap，这样可以保证每次pop出来的都是最小的。
O(Klog(min(2K, N)), O(min(2K, N)), 2K的原因是每次最多放两个数，所以heap最多放入2K个数。
"""

import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return None

        n = len(matrix)
        heap = []
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        visited = set((0, 0))       # 注意这里的visited不能存储matrix[i][j]，因为不同的地方可能存在相同的数
        
        for _ in range(k):
            currMin, row, col = heapq.heappop(heap)
            if 0 <= row + 1 < n and (row + 1, col) not in visited:
                heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))
                visited.add((row + 1, col))
            if 0 <= col + 1 < n and (row, col + 1) not in visited:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
                visited.add((row, col + 1))
                
        return currMin
