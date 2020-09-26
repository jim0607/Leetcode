"""
689. Maximum Sum of 3 Non-Overlapping Subarrays

In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:

Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
"""




"""
DP solution is somehow similar with 123. Best Time to Buy and Sell Stock III.
sub_1_sum, sub_2_sum, sub_3_sum represent the sum of 1st k nums, 1st + 2nd k nums, 1st + 2nd + 3rd k nums.
max_1_sum, max_2_sum, max_3_sum represent the max sum of 1st k nums, 1st + 2nd k nums, 1st + 2nd + 3rd k nums.
update the max_1_sum, max_2_sum, max_3_sum as we travel through the array.
"""
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # initializetion
        sub_1_sum = sum(nums[:k])
        sub_2_sum = sum(nums[k:2*k])
        sub_3_sum = sum(nums[2*k:3*k])
        
        max_1_sum = sub_1_sum
        max_2_sum = max_1_sum + sub_2_sum
        max_3_sum = max_2_sum + sub_3_sum
        
        sub_1_idx, sub_2_idx, sub_3_idx = 0, k, 2 * k
        max_1_idx = sub_1_idx
        max_2_idx = [max_1_idx, sub_2_idx]
        max_3_idx = max_2_idx + [sub_3_idx]
        
        # dp: traverse the arr and update the max_1_sum, max_2_sum, max_3_sum as we go
        while sub_3_idx + k < len(nums):
            sub_1_sum = sub_1_sum + nums[sub_1_idx + k] - nums[sub_1_idx]
            sub_2_sum = sub_2_sum + nums[sub_2_idx + k] - nums[sub_2_idx]
            sub_3_sum = sub_3_sum + nums[sub_3_idx + k] - nums[sub_3_idx]

            if sub_1_sum > max_1_sum:
                max_1_sum = sub_1_sum
                max_1_idx = sub_1_idx + 1
            
            if sub_2_sum + max_1_sum > max_2_sum:
                max_2_sum = sub_2_sum + max_1_sum
                max_2_idx = [max_1_idx, sub_2_idx + 1]  # 不能独立更新idx, 因为这样的话对于例子 [1,1,1,1,1,1,1,999,1,1,1,1,1,1,1], 2 那就都挤到999那个数了，输出就变成了[6,6,6]
                                                        # 这样一起更新的话就是说只有max_1_sum导致了max_2_sum增大了才把max_1_idx更新进去，而独立更新是max_1_sum一但增大了就更新max_1_idx             
            if sub_3_sum + max_2_sum > max_3_sum:
                max_3_sum = sub_3_sum + max_2_sum
                max_3_idx = max_2_idx + [sub_3_idx + 1]
                
            sub_1_idx += 1
            sub_2_idx += 1
            sub_3_idx += 1
            
        return max_3_idx





"""
下面示范错误的更新方式 - 独立更新idx, 因为这样的话对于例子 [1,1,1,1,1,1,1,999,1,1,1,1,1,1,1], 2 那就都挤到999那个数了，输出就变成了[6,6,6]
"""
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # initializetion
        sub_1_sum = sum(nums[:k])
        sub_2_sum = sum(nums[k:2*k])
        sub_3_sum = sum(nums[2*k:3*k])
        
        max_1_sum = sub_1_sum
        max_2_sum = max_1_sum + sub_2_sum
        max_3_sum = max_2_sum + sub_3_sum
        
        sub_1_idx, sub_2_idx, sub_3_idx = 0, k, 2 * k
        max_1_idx, max_2_idx, max_3_idx = sub_1_idx, sub_2_idx, sub_3_idx
        
        # dp: traverse the arr and update the max_1_sum, max_2_sum, max_3_sum as we go
        while sub_3_idx + k < len(nums):
            sub_1_sum = sub_1_sum + nums[sub_1_idx + k] - nums[sub_1_idx]
            sub_2_sum = sub_2_sum + nums[sub_2_idx + k] - nums[sub_2_idx]
            sub_3_sum = sub_3_sum + nums[sub_3_idx + k] - nums[sub_3_idx]

            if sub_1_sum > max_1_sum:
                max_1_sum = sub_1_sum
                max_1_idx = sub_1_idx
            
            if sub_2_sum + max_1_sum > max_2_sum:
                max_2_sum = sub_2_sum + max_1_sum
                max_2_idx = sub_2_idx       # 这是错误的更新方式 - 独立更新idx, 因为这样的话对于例子 [1,1,1,1,1,1,1,999,1,1,1,1,1,1,1], 2 那就都挤到999那个数了，输出就变成了[6,6,6]
                
            if sub_3_sum + max_2_sum > max_3_sum:
                max_3_sum = sub_3_sum + max_2_sum
                max_3_idx = sub_3_idx
                
            sub_1_idx += 1
            sub_2_idx += 1
            sub_3_idx += 1
            
        return [max_1_idx + 1, max_2_idx + 1, max_3_idx + 1]
