347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


"""O(N+ClogK+K)
heapq, heapq中放入的是(freq, key)对
需要一个cntDict来记录cnt先"""

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums
        
        cntDict = {}
        for num in nums:                            # O(N)
            if num in cntDict.keys():
                cntDict[num] += 1
            else:
                cntDict[num] = 1
                
        heap = []
        # algorithm is the same as 215: Kth largest element in array
        for num, freq in cntDict.items():           # O(C), C is the size of cntDict
            heapq.heappush(heap, (freq, num))       # O(K), K is the size of heap
            if len(heap) > k:
                heapq.heappop(heap)
                
        res = []
        for freq, num in heap:
            res.append(num)
            
        return res[::-1]                        # O(K)
