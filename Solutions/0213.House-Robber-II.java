213. House Robber II

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.



class Solution {
    public int rob(int[] nums) {
        int lens = nums.length;
        if (lens == 0) return 0;
        if (lens == 1) return nums[0];
        
        int currMax = 0, prevMax = 0;
        for (int i = 1; i < lens; i++) {
            int temp = currMax;
            currMax = Math.max(currMax, prevMax + nums[i]);
            prevMax = temp;
        }
        
        int res = currMax;
        
        currMax = 0; prevMax = 0;
        for (int i = 0; i < lens - 1; i++) {
            int temp = currMax;    // 这里必须再次声明temp的类型，上一个for循环真的是啥变量都带不出来。
            currMax = Math.max(currMax, prevMax + nums[i]);
            prevMax = temp;
        }
        
        res = Math.max(res, currMax);
        
        return res;
    }
}
