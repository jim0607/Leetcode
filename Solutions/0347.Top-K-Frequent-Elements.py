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

"""
"""O(N+ClogK+K)
heapq, heapq中放入的是(freq, key)对
需要一个cntDict来记录cnt先"""

from heapq import heappush, heappop, heapify

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        
        # algorithm is the same as 215: Kth largest element in array
        hq = []
        for num, cnt in counter.items():
            heappush(hq, (cnt, num))    #把freq放在num前面是为了用freq作为标准来做heap的排序, O(logK), K is the size of heap
            if len(hq) > k:
                heappop(hq)
                
        return [num for cnt, num in hq]
        
    
    
""""use heapify to realize O(N) solution"""

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsFreq = collections.defaultdict(int)
        for num in nums:
            numsFreq[num] += 1
            
        hq = []
        for num, freq in numsFreq.items():
            hq.append((-freq, num))
            
        heapq.heapify(hq)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(hq)[1])
            
        return res
    
    
    
"""
solution 2: quick select - O(N)
"""

"""
solution 3: bucket sort - O(N)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        max_freq = max(freq.values())   # 
        
        # we use max_freq as our bucket size
        # we use a list of num with frequency=i at idx i
        bucket = [[] for _ in range(max_freq + 1)]    
        
        for num, cnt in freq.items():
            bucket[cnt].append(num)   # 把freq当做idx来放入bucket中，这样一来high freq的ch就天然的放在bucket后面了, 就不需要sort了
        
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
