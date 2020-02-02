338. Counting Bits

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]


"""状态f[i]=i的二进制中有多少个1
和位操作相关的动态规划一般用值作为状态
转移方程f[i] = f[i>>1] + i%2
i>>1表示i往右移动一位，最后一位就撞到墙了就撞没了。
初始条件为f[0]=0
O(N)， O（N）"""
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i >> 1] + i % 2  
            
        return dp
