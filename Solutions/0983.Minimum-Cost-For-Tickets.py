"""
983. Minimum Cost For Tickets

In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
"""



"""
是一个简单的动态规划问题。我们定义函数f(i)表示第i天的最低消费，那么
某天，如果你不必出行的话，等一等再购买火车票一定更优，如果你需要出行的话，那么就有三种选择：在通行期为 1 天、7 天、30 天中的火车票中选择一张购买。
f(i)=f(i−1)  if i not in days
else f(i)=min(f(i−1)+costs[0],f(i−7)+costs[1],f(i−30)+costs[2])
"""
"""
dp[i] = min cost from 0 day to day i.
If day i is not one of our days, then we don't have to worry. The cost is the same as the cost to cover all days to day i-1 => dp[n] = dp[n-1]
If day i is one of our days, then we will check if buying a pass before can help us minimize the cost.
For example, buying a week-pass a week ago can cost: dp[n-7] + costs[1].
dp[i] = min(dp[i-1] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0, i-30)] + costs[2])
"""
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_set = set(days)
        dp = [0 for _ in range(days[-1] + 1)]   # min cost from 0 day to day i
        for i in range(1, len(dp)):
            if i not in days_set:
                dp[i] = dp[i-1]
                continue
            dp[i] = min(dp[i-1] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0, i-30)] + costs[2])
        return dp[-1]
