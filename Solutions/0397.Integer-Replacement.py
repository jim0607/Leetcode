"""
397. Integer Replacement

Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.

Example 1:

Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1
Example 2:

Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1
Example 3:

Input: n = 4
Output: 2
"""


"""
单源节点出发的bfs: log(N)
"""
class Solution:
    def integerReplacement(self, n: int) -> int:
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
                if curr_num == 1:
                    return steps
                
                if curr_num % 2 == 0 and curr_num // 2 not in visited:
                    q.append(curr_num // 2)
                    visited.add(curr_num // 2)
                if curr_num + 1 not in visited:
                    q.append(curr_num + 1)
                    visited.add(curr_num + 1)
                if curr_num - 1 not in visited:
                    q.append(curr_num - 1)
                    visited.add(curr_num - 1)


"""
这类题的首选算法是BFS, 因为BFS只需要闭着眼睛一步一步往前就可以了。
而backtrack + memo的方法需要贪心判断不能除2才能进行+1或-1的操作！否则会导致算法degrade to O(N) TLE. 这里是很容易出错的！
backtrack end condition: curr_num == 1
constraints on next_candidates: can be curr_num//2, curr_num+-1
arguments pass into backtrack function: curr_num, curr_steps
O(log(N))
"""
"""
backtrack end condition: curr_num == 1
constraints on next_candidates: can be curr_num//2, curr_num+-1
arguments pass into backtrack function: curr_num, curr_steps
"""
class Solution:
    def integerReplacement(self, n: int) -> int:
        def backtrack(curr_num, curr_steps):
            if curr_num == 1:
                self.min_steps = min(self.min_steps, curr_steps)
                return
            
            if curr_steps >= self.min_steps:    # strong pruning, which I learnt from 1240. Tiling a Rectangle with the Fewest Squares
                return
            
            if curr_num % 2 == 0:
                backtrack(curr_num // 2, curr_steps + 1)
            else:       # 注意要不能除2才选择 +1或-1, 核心算法是能除就除，不能除才+1或-1
                backtrack(curr_num + 1, curr_steps + 1)
                backtrack(curr_num - 1, curr_steps + 1)
                        
            
        self.min_steps = sys.maxsize
        backtrack(n, 0)
        return self.min_steps
    
    
    
"""
memo: O(logN)
"""
class Solution:
    def integerReplacement(self, n: int) -> int:
        def backtrack(curr_num):
            if curr_num == 1:
                return 0
            
            if curr_num in memo:
                return memo[curr_num]
            
            res = sys.maxsize
            if curr_num % 2 == 0:
                res = min(res, 1 + backtrack(curr_num // 2))
            else:       # 注意要不能除2才选择 +1或-1, 核心算法是能除就除，不能除才+1或-1
                res = min(res, 1 + backtrack(curr_num + 1))
                res = min(res, 1 + backtrack(curr_num - 1))
                
            memo[curr_num] = res
            return res
                        
            
        memo = defaultdict(int) # curr_num --> from curr_num, min_steps to reach 1
        return backtrack(n)
