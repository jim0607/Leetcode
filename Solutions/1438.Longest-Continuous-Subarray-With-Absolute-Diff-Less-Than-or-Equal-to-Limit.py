"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
"""


"""
如果题目需要我们在window里更新最大值或最小值，我们往往需要maintian一个mono increasing or mono decreasing deque.
这个题目我们maintain an increasing dq and a decreasing dq.
"""
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxdq = collections.deque()     # decreasing dq
        mindq = collections.deque()     # increasing dq
        i = 0       # 窗口的起点
        res = 0
        for j, num in enumerate(nums):
            # step 1: 更新maxdq, just like what we did for monostack
            while len(maxdq) > 0 and maxdq[-1] < num:
                maxdq.pop()
            maxdq.append(num)
            
            # step 2: 更新mindq, 套用mono stack模板
            while len(mindq) > 0 and mindq[-1] > num:
                mindq.pop()
            mindq.append(num)
            
            # step 3: sliding window to update res - 套用sliding window模板
            while maxdq[0] - mindq[0] > limit:
                # if > limit, then it means we need to move i forward, before moving i forward 
                # we might need to delete nums[i] if it is in the maxdq or mindq
                if nums[i] == maxdq[0]:
                    maxdq.popleft()
                if nums[i] == mindq[0]:
                    mindq.popleft()
                i += 1
                
            if maxdq[0] - mindq[0] <= limit:
                res = max(res, j - i + 1)
                
        return res
