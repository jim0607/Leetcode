"""
1326. Minimum Number of Taps to Open to Water a Garden

There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.

Example 1:


Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]
Example 2:

Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water the whole garden.
Example 3:

Input: n = 7, ranges = [1,2,1,0,2,1,0,1]
Output: 3
Example 4:

Input: n = 8, ranges = [4,0,0,0,0,0,0,0,4]
Output: 2
Example 5:

Input: n = 8, ranges = [4,0,0,0,4,0,0,0,4]
Output: 1
"""



"""
We build a list reachable to store the max range it can be watered from each index.
Then it becomes Jump Game II, where we want to find the minimum steps to jump from 0 to n.
每跳一步就相当于开一个水龙头
"""
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # step 1: build the reachable list
        reachable = [0 for _ in range(n + 1)]      # reachable[idx] = start from idx, where we can reach
        for i, ran in enumerate(ranges):
            idx = max(0, i - ran)       
            reachable[idx] = max(reachable[idx], i + ran)   
            
        # step 2: now it's Jump Game II, we need to find the min steps to jump from 0 to n
        last_coverage = 0
        next_coverage = reachable[0]
        cnt = 0
        i = 0
        while i < n + 1:
            while i <= last_coverage:
                next_coverage = max(next_coverage, reachable[i])
                i += 1
            
            if next_coverage == last_coverage:      # 不能往前进了说明无法cover所有
                return -1
            last_coverage = next_coverage
            
            cnt += 1
            if next_coverage >= n:
                return cnt
