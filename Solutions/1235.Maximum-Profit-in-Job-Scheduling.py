"""
1235. Maximum Profit in Job Scheduling

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime , endTime and profit arrays, you need to output the maximum profit 
you can take such that there are no 2 jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

Example 1:

Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:

Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
Example 3:

Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
 
Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4
"""



"""
similar with 646. Maximum Length of Pair Chain, we define dp as
dp[i] = the max_prof for intervals ended with ith interval;
dp[j] = max(dp[i] + profit[j] for i < j if endTime[i] <= startTime[j]).
return max(dp)
O(N^2) - TLE
"""
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        intervals = [[startTime[i], endTime[i], profit[i]] for i in range(n)]
        intervals.sort(key = lambda x: (x[1], x[0]))
        
        dp = [intervals[i][2] for i in range(n)]
        for j in range(1, n):
            for i in range(j):
                if intervals[i][1] <= intervals[j][0]:
                    dp[j] = max(dp[j], dp[i] + intervals[j][2])
        return max(dp)
        
        
"""
在进入binary seach solution 之前，我们将dp定义为
dp[i] = the max_prof for intervals before (including) ith interval;
dp[j] = max(profit[j], dp[i] + profit[j] for i < j if endTime[i] <= startTime[j]).
return dp[-1]
O(N^2)
"""
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        intervals = [[startTime[i], endTime[i], profit[i]] for i in range(n)]
        intervals.sort(key = lambda x: (x[1], x[0]))
        
        dp = [intervals[i][2] for i in range(n)]
        for j in range(1, n):
            dp[j] = max(dp[j], dp[j-1])     # 只加入jth一个interval vs. 不加入jth interval
            for i in range(j):              # vs. 只加入jth一个interval和前面i个interval
                if intervals[i][1] <= intervals[j][0]:
                    dp[j] = max(dp[j], dp[i] + intervals[j][2])
        return dp[-1]
        
        
        
"""
由于我们是要在i < j且满足intervals[i][1] <= intervals[j][0]的i中选一个max(dp[i]).
由于我们定义dp[i] = the max_prof for intervals before (including) ith interval,
所以dp是递增的，所以只需要在dp[:j]中选最后一个满足intervals[i][1] <= intervals[j][0]的i就可以了
所以想到用binary search.
O(NlogN)
"""
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        intervals = [[startTime[i], endTime[i], profit[i]] for i in range(n)]
        intervals.sort(key = lambda x: (x[1], x[0]))
        
        dp = [intervals[i][2] for i in range(n)]
        for j in range(1, n):
            dp[j] = max(dp[j], dp[j-1])     # 只加入jth一个interval vs. 不加入jth interval
            i = self._binary_search(intervals, j)   
            if i != -1:
                dp[j] = max(dp[j], intervals[j][2] + dp[i])   # vs. 只加入jth一个interval和前面i个interval
        return dp[-1]
    
    def _binary_search(self, intervals, target_idx):
        """
        Return the last idx in intervals that satisfy intervals[idx][1] <= intervals[target_idx][0]
        """
        start, end = 0, target_idx - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if intervals[mid][1] <= intervals[target_idx][0]:
                start = mid
            else:
                end = mid
        if intervals[end][1] <= intervals[target_idx][0]:
            return end
        if intervals[start][1] <= intervals[target_idx][0]:
            return start
        return -1       # return -1表示j前面找不到一个valid i
