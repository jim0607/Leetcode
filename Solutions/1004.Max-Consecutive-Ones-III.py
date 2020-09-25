"""
1004. Max Consecutive Ones III

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
"""



"""
longest subarray with at most one 0s. 这题是at most problem, 写法是while loop里让前面的指针去追后面的指针. 
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_lens = 0
        zero_cnt = 0
        i = 0
        for j in range(len(nums)):
            zero_cnt += 1 if nums[j] == 0 else 0
            
            while i <= j and zero_cnt > k:
                zero_cnt -= 1 if nums[i] == 0 else 0
                i += 1
                
            if zero_cnt <= k:
                max_lens = max(max_lens, j - i + 1)
                
        return max_lens
