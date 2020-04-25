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
        freqDict = collections.defaultdict(int)
        for num in nums:        # O(N)
            freqDict[num] += 1
            
        # algorithm is the same as 215: Kth largest element in array
        freqHeapq = []
        for num, freq in freqDict.items():          # # O(C), C is the size of cntDict
            heapq.heappush(freqHeapq, (freq, num))  #把freq放在num前面是为了用freq作为标准来做heap的排序, O(K), K is the size of heap
            if len(freqHeapq) > k:
                heapq.heappop(freqHeapq)
        
        res = []
        for (freq, num) in freqHeapq:
            res.append(num)
            
        return res[::-1]        # O(K)
