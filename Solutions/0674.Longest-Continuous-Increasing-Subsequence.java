674. Longest Continuous Increasing Subsequence

Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 




class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int lens = nums.length;
        if (lens <= 1) return lens;
        
        int[] dp = new int[lens];   // dp[i] = the LCIS lens until the ith
        dp[0] = 1;
        
        int res = 1;
        for (int i = 1; i < lens; i++) {
            if (nums[i] > nums[i - 1]) {
                dp[i] = dp[i - 1] + 1;
            } else {
                dp[i] = 1;
            }
            res = Math.max(res, dp[i]);
        }
        
        return res;
    }
}



class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int lens = nums.length;
        if (lens <= 1) return lens;
        
        int dp = 1;
        int res = 1;
        
        for (int i = 1; i < lens; i++) {
            int temp = dp;
            if (nums[i] > nums[i - 1]) {
                dp = temp + 1;
            } else {
                dp = 1;
            }
            res = Math.max(res, dp);
        }
        
        return res;
    }
}
