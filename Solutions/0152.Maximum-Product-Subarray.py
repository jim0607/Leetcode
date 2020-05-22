152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lens = len(nums)
        maxDP = [0] * lens      # maxDP[i]表示以i为结尾的subarray的最product
        minDP = [0] * lens      # 记录最小的负数
        maxDP[0], minDP[0] = nums[0], nums[0]
        for i in range(1, lens):    # 特别注意遍历不要包括初始状态
            if nums[i] >= 0:
                maxDP[i] = max(nums[i], maxDP[i - 1] * nums[i])
                minDP[i] = min(nums[i], minDP[i - 1] * nums[i])
                
            else:
                maxDP[i] = max(nums[i], minDP[i - 1] * nums[i])
                minDP[i] = min(nums[i], maxDP[i - 1] * nums[i])
                
        return max(maxDP)

    
    
public class Solution {
    public int MaxProduct(int[] nums) {
        int lens = nums.Length;
        int[] maxDP = new int[lens];  // maxDP[i]表示以i为结尾的subarray的最product
        int[] minDP = new int[lens];
        maxDP[0] = nums[0];
        minDP[0] = nums[0];
            
        for (int i = 1; i < lens; i++) {
            if (nums[i] >= 0) {
                maxDP[i] = Math.Max(nums[i], nums[i] * maxDP[i - 1]);
                minDP[i] = Math.Min(nums[i], nums[i] * minDP[i - 1]);
            }
            else {
                maxDP[i] = Math.Max(nums[i], nums[i] * minDP[i - 1]);
                minDP[i] = Math.Min(nums[i], nums[i] * maxDP[i - 1]);
            }
        }
        
        return maxDP.Max();
    }
}
