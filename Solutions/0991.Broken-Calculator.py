"""
991. Broken Calculator

On a broken calculator that has a number showing on its display, we can perform two operations:

Double: Multiply the number on the display by 2, or;
Decrement: Subtract 1 from the number on the display.
Initially, the calculator is displaying the number X.

Return the minimum number of operations needed to display the number Y.

Example 1:

Input: X = 2, Y = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
Example 2:

Input: X = 5, Y = 8
Output: 2
Explanation: Use decrement and then double {5 -> 4 -> 8}.
Example 3:

Input: X = 3, Y = 10
Output: 3
Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.
Example 4:

Input: X = 1024, Y = 1
Output: 1023
Explanation: Use decrement operations 1023 times.
"""


"""
先将y除下来，除到y < x之后再减，出的过程中遇到y为奇数就加一
eg: x = 5, y = 120. 
y // 2 = 60; step = 1
y // 2 = 30; step = 2
y // 2 = 15; step = 3
y = y + 1;   step = 4   # 遇到y为奇数就加一，不能减一因为对x的操作只能是减一，所以对y的操作只能是加一
y // 2 = 8;  step = 5
y // 2 = 4;  step = 6
出while loop cuz y < x; step += x - y
"""
class Solution:
    def brokenCalc(self, x: int, y: int) -> int:
        step = 0
        while y > x:
            if y % 2 == 0:
                y //= 2         # O(log(Y))
            else:
                y += 1
            step += 1
        return step + x - y
    
"""
注意这题不能将x乘上去，将x乘上去肯定没有将y除下来步数更少，eg:x = 1, y = 80, x 乘上去会变成64，距离100还有16步；而将100除下来会变成5，距离1只有4步
"""

"""
单源节点出发最短路径问题：bfs
"""
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        q = deque()
        visited = set()
        q.append(Y)
        visited.add(Y)
        
        steps = -1
        while len(q) > 0:
            steps += 1
            lens = len(q)
            for _ in range(lens):
                curr_Y = q.popleft()
                if curr_Y <= X:     # 注意如果curr_Y < X的话直接可以return 了, 否则TLE
                    return steps + X - curr_Y
                
                elif curr_Y > X:
                    if curr_Y % 2 == 0 and curr_Y // 2 not in visited:
                        q.append(curr_Y // 2)
                        visited.add(curr_Y // 2)
                    if curr_Y + 1 not in visited:
                        q.append(curr_Y + 1)
                        visited.add(curr_Y + 1)
                        
"""
backtrack end condition: if curr_Y <= X
constraints on next_candidates: could be curr_Y // 2 or curr_Y + 1
arguments pass into backtrack function: curr_steps
"""
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        def backtrack(curr_Y, curr_steps):
            if curr_Y <= X:
                self.min_steps = min(self.min_steps, curr_steps + X - curr_Y)
                return
            
            if curr_Y % 2 == 0:
                backtrack(curr_Y // 2, curr_steps + 1)
            else:               # 注意要不能除2才加一
                backtrack(curr_Y + 1, curr_steps + 1)
            
            
        self.min_steps = sys.maxsize
        backtrack(Y, 0)
        return self.min_steps
    
    
"""
recursion + memo: log(Y)
"""
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        def backtrack(curr_Y):
            if curr_Y <= X:
                return X - curr_Y
            
            if curr_Y in memo:
                return memo[curr_Y]
            
            res = sys.maxsize
            if curr_Y % 2 == 0:
                res = min(res, 1 + backtrack(curr_Y // 2))
            else:               # 注意要不能除2才加一
                res = min(res, 1 + backtrack(curr_Y + 1))
                
            memo[curr_Y] = res
            return res
            
            
        memo = defaultdict(int)  # curr_Y --> from curr_Y, min_steps to reach X
        return backtrack(Y)
