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
                y //= 2
            else:
                y += 1
            step += 1
        return step + x - y
    
"""
注意这题不能将x乘上去，将x乘上去肯定没有将y除下来步数更少，eg:x = 1, y = 80, x 乘上去会变成64，距离100还有16步；而将100除下来会变成5，距离1只有4步
"""



"""
单源节点出发最短路径问题：bfs - O(2^(Y-X))  TLE
"""
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        q = collections.deque()
        visited = set()
        q.append(X)
        visited.add(X)
        steps = -1
        while len(q) > 0:
            lens = len(q)
            steps += 1
            for _ in range(lens):
                curr = q.popleft()
                if curr == Y:
                    return steps
                
                for next in [curr * 2, curr - 1]:
                    if next not in visited:
                        q.append(next)
                        visited.add(next)
