"""
1231. Divide Chocolate

You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your K friends so you start cutting the chocolate bar into K+1 pieces using K cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.


Example 1:

Input: sweetness = [1,2,3,4,5,6,7,8,9], K = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
Example 2:

Input: sweetness = [5,6,7,8,9,1,2,3,4], K = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.
Example 3:

Input: sweetness = [1,2,2,1,2,2,1,2,2], K = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
"""



"""
Divide the nums into K+1 subarrays, and make sure each subarray has a sum at least S.
Find the max S. so it's a OOXXX problem finding the last O.
Use greedy to check can get - O(N).  Overall: O(NlogM), where N = len(sweetness), M = sum(sweetness)//(K+1)
"""
class Solution:
    def maximizeSweetness(self, nums: List[int], K: int) -> int:
        start, end = min(nums), sum(nums) // (K+1) + 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._can_divide(nums, K+1, mid):
                start = mid
            else:
                end = mid
        return end if self._can_divide(nums, K+1, end) else start   # 注意是return end在前面，因为需要求的是能得到的最大值
    
    def _can_divide(self, nums, k, min_sum):
        cnt = 0     # how many subarrays can get a sum at least min_sum
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum >= min_sum:
                cnt += 1
                curr_sum = 0
        return cnt >= k
