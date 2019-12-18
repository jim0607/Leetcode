We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose any two rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone (the weight is 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0 so the array converts to [1] then that's the optimal value.


"""由于石头拿走还能放回去，因此可以简单地把所有石头看作两堆
假设总重量为 sum, 则问题转化为背包问题：
如何使两堆石头总重量接近 sum / 2
dp[i] 背包容量限制为 i 时能够装载的最大石块总重量
curStone 存在最优解 dp[i] 时需要考虑的下一块石块重量"""
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        lens = len(stones)
        maxCapacity = sum(stones)//2
        dp = [0] * (maxCapacity+1)
        for i in range(lens):
            currStone = stones[i]
            for j in range(maxCapacity, currStone-1, -1):
                dp[j] = max(dp[j], dp[j-currStone] + currStone)
        return sum(stones) - 2 * dp[maxCapacity]
