55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


"""O(N^2), O(N)"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)    # 确定状态：dp[j]表示能不能跳到位置j
        dp[0] = True                # 初始条件
        for j in range(1, len(nums)):
            for i in range(j):
                if dp[i] and i + nums[i] >= j:  # 转移方程：只要在dp[j]之前存在一个dp[i]=True且从这个i位置够得着j位置，那么dp[j]就为True
                    dp[j] = True
                    break
        
        return dp[-1]
    
"""TLE, should try Greedy solution with O(N), O(1)"""

"""Greedy 解法: O(N) 
Iterating right-to-left, for each position we check if there is a potential jump that 
reaches a GOOD index (currPosition + nums[currPosition] >= GoodIndex). If we can reach a GOOD index, 
then our position is itself GOOD. Iteration continues until the beginning of the array.  
Return if the first position is a GOOD index."""
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lens = len(nums)
        goodPos = lens - 1
        for i in range(lens - 1, -1, -1):
            if i + nums[i] >= goodPos:
                goodPos = i
                
        return goodPos == 0

    
"""
也可以从前往后遍历
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lens = len(nums)
        maxPos = nums[0]    # max position one could reach 
        for i in range(1, lens):
            if maxPos < i:  # if couldnot reach this point
                return False
            
            maxPos = max(maxPos, nums[i] + i)
        
        return True





// C# solution does not TLE
public class Solution {
    public bool CanJump(int[] nums) {
        int lens = nums.Length;
        bool[] dp = new bool[lens];  // dp[i]表示能否调到第i个位置
        dp[0] = true;
        for (int i = 1; i < lens; i++) {
            dp[i] = false;
        }
        
        for (int j = 1; j < lens; j++) {
            for (int i = 0; i < j; i++) {
                if (dp[i] && nums[i] >= j - i) {
                    dp[j] = true;
                }
            }
        }
        
        return dp[lens - 1];
    }
}
