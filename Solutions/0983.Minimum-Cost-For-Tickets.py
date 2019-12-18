In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.


"""是一个简单的动态规划问题。我们定义函数f(i)表示第i天的最低消费，那么
某天，如果你不必出行的话，等一等再购买火车票一定更优，如果你需要出行的话，那么就有三种选择：在通行期为 1 天、7 天、30 天中的火车票中选择一张购买。
f(i)=f(i−1)  if i not in days
else f(i)=min(f(i−1)+costs[0],f(i−7)+costs[1],f(i−30)+costs[2])"""
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        lens = len(days)
        if lens == 0:
            return 0
        dp = [0] * 366
        days_set = set(days)
        for i in range(1, 366):
            if i not in days_set:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1]+costs[0], dp[i-7]+costs[1], dp[i-30]+costs[2])
        return dp[days[-1]]
