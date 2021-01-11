"""
1553. Minimum Number of Days to Eat N Oranges

There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:

Eat one orange.
If the number of remaining oranges (n) is divisible by 2 then you can eat  n/2 oranges.
If the number of remaining oranges (n) is divisible by 3 then you can eat  2*(n/3) oranges.
You can only choose one of the actions per day.

Return the minimum number of days to eat n oranges.

Example 1:

Input: n = 10
Output: 4
Explanation: You have 10 oranges.
Day 1: Eat 1 orange,  10 - 1 = 9.  
Day 2: Eat 6 oranges, 9 - 2*(9/3) = 9 - 6 = 3. (Since 9 is divisible by 3)
Day 3: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. 
Day 4: Eat the last orange  1 - 1  = 0.
You need at least 4 days to eat the 10 oranges.
Example 2:

Input: n = 6
Output: 3
Explanation: You have 6 oranges.
Day 1: Eat 3 oranges, 6 - 6/2 = 6 - 3 = 3. (Since 6 is divisible by 2).
Day 2: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. (Since 3 is divisible by 3)
Day 3: Eat the last orange  1 - 1  = 0.
You need at least 3 days to eat the 6 oranges.
"""


"""
bfs: O(n)
"""
class Solution:
    def minDays(self, n: int) -> int:
        q = deque()
        visited = set()
        q.append(n)
        visited.add(n)
        
        step = -1
        while len(q) > 0:
            step += 1
            lens = len(q)
            for _ in range(lens):
                curr_n = q.popleft()
                if curr_n == 0:
                    return step
                
                if curr_n - 1 not in visited:
                    q.append(curr_n - 1)
                    visited.add(curr_n - 1)
                if curr_n % 2 == 0:
                    q.append(curr_n // 2)
                    visited.add(curr_n // 2)
                if curr_n % 3 == 0:
                    q.append(curr_n // 3)
                    visited.add(curr_n // 3)
                    

"""
backtrack结束条件: curr_n == 0
constraints on next_candidate: can have three different options to eat
arguments pass into backtrack function: curr_n
"""
class Solution:
    def minDays(self, n: int) -> int:
        def backtrack(curr_n, curr_days):
            if curr_n == 0:
                self.min_days = min(self.min_days, curr_days)
                return
            
            backtrack(curr_n - 1, curr_days + 1)
            if curr_n % 2 == 0:
                backtrack(curr_n // 2, curr_days + 1)
            if curr_n % 3 == 0:
                backtrack(curr_n // 3, curr_days + 1)

            
        self.min_days = n
        backtrack(n, 0)
        return self.min_days

"""
memorization - O(N)
"""
class Solution:
    def minDays(self, n: int) -> int:
        def backtrack(curr_n):
            if curr_n == 0:
                return 0
            
            if curr_n in memo:
                return memo[curr_n]
            
            res = curr_n
            res = min(res, 1 + backtrack(curr_n - 1))
            if curr_n % 3 == 0:
                res = min(res, 1 + backtrack(curr_n // 3))
            elif curr_n % 2 == 0:
                res = min(res, 1 + backtrack(curr_n // 2))

            memo[curr_n] = res
            return res

            
        memo = defaultdict(int)     # curr_n --> how many days to eat curr_n
        return backtrack(n)
