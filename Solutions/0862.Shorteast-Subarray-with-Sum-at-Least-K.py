"""
862. Shortest Subarray with Sum at Least K

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
"""



"""
不能像209. Minimum Size Subarray Sum那样用sliding window因为209那题是positive numbers, 这题可以为负值。
这题的最优解是mono deque. O(N). 先构造一个presum list, 接下来方法与239类似的，
两个while循环，一个while loop do sliding window to update res, 从队首pop, 同时更新res, 
另一个while loop do monostack to maintain an increasing dq, 从队尾pop, 对deq进行清理。
"""
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        # step 1: construct a presum list
        lens = len(A)
        presum = [0 for _ in range(lens + 1)]
        for i, num in enumerate(A):
            presum[i+1] = presum[i] + num
        
        # step 2: use the presum to do sliding window on a mono increasing dq
        dq = deque()     # maintain a mono increasing dq, dq存(val, idx) pair
        min_len = float("inf")
        for i, pre in enumerate(presum):
            
            # firstly, we pop from left to update res just like sliding window
            while len(dq) > 0 and pre - dq[0][0] >= K:
                idx = dq.popleft()[1]
                min_len = min(min_len, i - idx)
                
            # secondly, we pop from right to maintain a mono increasing dq just like monostack
            # 把现在这个pre push进deq之前，把deq尾部的比现在这个pre要大的presum给pop出来，
            # 因为由于这个pre的存在，这些尾部的都再也用不上了, 因为后面的计算中这些尾部的值又大离后面的数又远 
            while len(dq) > 0 and pre <= dq[-1][0]:
                dq.pop()
            dq.append((pre, i))
            
        return min_len if min_len != float("inf") else -1
    
    
"""
注意binary search是行不通的，因为 [10, -5, 5], K = 9 的情况，
mid_L = 2 不行，但是这不意味着 L = 1 不行，也意味着 L = 3 不行
"""
