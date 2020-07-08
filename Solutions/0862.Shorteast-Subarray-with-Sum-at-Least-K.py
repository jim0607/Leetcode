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
不能像209. Minimum Size Subarray Sum那样用sliding window因为209那题是positive numbers, 这题可以为负值。
这题的最优解是mono deque. O(N). 方法与239类似的，两个while循环，一个从队首pop, 同时更新res, 另一个从队尾pop, 对deq进行清理。
"""
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        lens = len(A)
        presum = [0 for _ in range(lens + 1)]
        for i, num in enumerate(A):
            presum[i+1] = presum[i] + num
            
        res = float("inf")
        deq = collections.deque()   # deq store the idx in the presum
        for i, pre in enumerate(presum):
            while deq and pre - presum[deq[0]] >= K:    # 注意这里是pop出deq[0]队首的presum
                idx = deq.popleft()
                res = min(res, i - idx)
                
            # 把现在这个pre push进deq之前，把deq尾部的比现在这个pre要大的presum给pop出来，因为由于这个pre的存在，这些尾部的都用上了, 
            # 这里跟上一题是一样的，都是从队尾进行pop的
            while deq and presum[deq[-1]] >= pre:
                deq.pop()
                
            deq.append(i)
            
        return res if res != float("inf") else -1
