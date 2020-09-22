"""
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



"""
solution 3: bucket sort - O(N). bucket sort is garanteed to be O(N), while quick select is O(N) ot O(N^2)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        
        max_cnt = max(cnt for cnt in counter.values())  # we use max_freq as our bucket size
        freq_to_num = [[] for _ in range(max_cnt + 1)]  
        for num, cnt in counter.items():
            freq_to_num[cnt].append(num)    # 把freq当做idx来放入bucket中，
                                        # 这样一来high freq的ch就天然的放在bucket后面了, 就不需要sort了
        res = []
        for i in range(len(freq_to_num) - 1, -1, -1):
            if len(freq_to_num) > 0:
                res += freq_to_num[i]
            if len(res) == k:
                return res


"""
O(N+ClogK+K)
heapq, heapq中放入的是(freq, key)对
需要一个cntDict来记录cnt先
"""

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
        
      
    
    
"""
solution 2: quick select - O(N)
"""


