"""
525. Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""



"""
将0都变成-1，题目就变成了max subarray size with sum == 0.
由于arr中有正数有负数，所以不能用sliding window, 只能用prefix sum + hashmap
"""
class Solution:
    def findMaxLength(self, arr: List[int]) -> int:
        nums = [-1 if arr[i] == 0 else 1 for i in range(len(arr))]
            
        max_lens = 0
        pre_sum = 0
        pre_sum_dict = collections.defaultdict(int)     # pre_sum --> idx where the pre_sum occured
        pre_sum_dict[0] = -1        # 注意别忘了初始化
        for i, num in enumerate(nums):
            pre_sum += num
            
            if pre_sum in pre_sum_dict:
                max_lens = max(max_lens, i - pre_sum_dict[pre_sum])
            
            else:             # 只有当pre_sum not in pre_sum_dict我们才更新pre_sum_dict[pre_sum]，
                pre_sum_dict[pre_sum] = i   # 这是为了保证idx尽可能小，这样max_lens才能尽可能大
                
        return max_lens
