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
bfs: O(logN) because each step we on average can get rid of n/2 nodes.
"""
class Solution:
    def minDays(self, n: int) -> int:
        q = deque()
        visited = set()
        q.append(n)
        visited.add(n)
        
        steps = -1
        while len(q) > 0:
            steps += 1
            lens = len(q)
            for _ in range(lens):
                curr_num = q.popleft()
                if curr_num == 0:
                    return steps
                
                if curr_num - 1 not in visited:
                    q.append(curr_num - 1)
                    visited.add(curr_num - 1)
                if curr_num % 2 == 0 and curr_num // 2 not in visited:
                    q.append(curr_num // 2)
                    visited.add(curr_num // 2)
                if curr_num % 3 == 0 and curr_num // 3 not in visited:
                    q.append(curr_num // 3)
                    visited.add((curr_num // 3))
                    

"""
backtrack end condition: curr_num == 0
constraints on next_candidates: next_num could be curr_num-1, curr_num//2 curr_num//3
arguments pass into backtrack: curr_num, curr_cnt
O(3^N) - TLE
"""
class Solution:
    def minDays(self, n: int) -> int:
        def backtrack(curr_num, curr_cnt):
            if curr_num == 0:
                self.min_cnt = min(self.min_cnt, curr_cnt)
                return
            
            backtrack(curr_num - 1, curr_cnt + 1)
            if curr_num % 2 == 0:
                backtrack(curr_num // 2, curr_cnt + 1)
            if curr_num % 3 == 0:
                backtrack(curr_num // 3, curr_cnt + 1)
                
                
        self.min_cnt = n
        backtrack(n, 0)
        return self.min_cnt

"""
memorization - O(logN)
这类题的首选算法是BFS, 因为BFS只需要闭着眼睛一步一步往前就可以了。
而backtrack + memo的方法需要贪心判断不能除2或除3才能进行-1的操作！否则会导致算法degrade to O(N) TLE. 这里是很容易出错的！
"""
class Solution:
    def minDays(self, n: int) -> int:
        def backtrack(curr_num):
            if curr_num == 0:
                return 0
            
            if curr_num in memo:
                return memo[curr_num]
            
            res = sys.maxsize
            if curr_num % 2 == 0:
                res = min(res, 1 + backtrack(curr_num // 2))
            if curr_num % 3 == 0:
                res = min(res, 1 + backtrack(curr_num // 3))
            if curr_num % 2 != 0 or curr_num % 3 != 0:      # !!!注意这里用or, eg: 10
                res = min(res, 1 + backtrack(curr_num - 1)) # !!! 注意不能不判断就直接curr_num - 1, 不然就O(N) TLE了
                
            memo[curr_num] = res
            return res
                
                
        memo = defaultdict(int)  # curr_num --> from curr_num, what's the minimum day to reach 0
        return backtrack(n)      # returns from curr_num, what's the minimum day to reach 0
