198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
             

class Solution {
    public int rob(int[] nums) {
        int lens = nums.length;
        if (lens == 0) return 0;
        
        int[] dp = new int[lens];   // dp[i] = the max profix when reach house i
        dp[0] = nums[0];
        if (lens == 1) return nums[0];
        dp[1] = Math.max(nums[0], nums[1]);
        
        for (int i = 2; i < lens; i++) {
            dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);
        }
        return dp[lens - 1];
    }
}
