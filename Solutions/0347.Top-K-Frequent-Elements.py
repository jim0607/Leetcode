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
        cnter = Counter(nums)
        cnt_to_num = [[] for _ in range(max(cnter.values()) + 1)]   # we use max_freq as our bucket size
        for num, cnt in cnter.items():      # 把freq当做idx来放入bucket中，
            cnt_to_num[cnt].append(num)     # 这样一来high freq的ch就天然的放在bucket后面了, 就不需要sort了
            
        res = []
        for i in range(len(cnt_to_num) - 1, -1, -1):
            res += cnt_to_num[i]
            if len(res) >= k:
                return res


"""
O(N+klogk)
heapq, heapq中放入的是(freq, key)对
需要一个cntDict来记录cnt先
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnter = Counter(nums)
        
        hq = [(-cnt, num) for num, cnt in cnter.items()]
        heapify(hq)
        
        res = []
        for _ in range(k):
            res.append(heappop(hq)[1])
            
        return res
        
      
    
    
"""
solution 2: quick select - O(N)
"""


