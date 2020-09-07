351. Android Unlock Patterns

Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

 

Rules for a valid pattern:

Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
The order of keys used matters.
 

Explanation:

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Invalid move: 4 - 1 - 3 - 6
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

Example:

Input: m = 1, n = 1
Output: 9




"""
This question is easy to implement if the nextNum from any num was in any of 8 possible directions. 
However, the tricky part is that the path to reach nextNum might go through existing numbers as well.
For example, 6 - 5 - 4 - 1 - 9 - 2 is a valid move. If you notice this sequence carefully, we are passing through 5 twice. 
This type of movement is different from the usual DFS in a matrix.
Technically, the screen unlocking on android devices have dots and not numbers. 
That makes it lot easier to understand how we can reach from 1 to 6 without going through 5. (or 2 to 9 without going through 5 or 6)
So, summarizing the above points: From a number in the keypad we can reach any other number, but can't reach the one's that have a number as obstacle in between. 
For example, for (1 to 3), the obstacle is 2.
cannot_pass = {(1, 3): 2, (3, 1): 2, (1, 7): 4, (7, 1): 4, (3, 9): 6, (9, 3): 6, (7, 9): 8, (9, 7): 8,
               (4, 6): 5, (6, 4): 5, (2, 8): 5, (8, 2): 5, (1, 9): 5, (9, 1): 5, (3, 7): 5, (7, 3): 5}
So, if you have to reach through the obstacle, it is possible only if the obstacle was previously visited.
If you just understand this, rest of the problem becomes easy to code.
"""
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        def backtrack(curr_num, curr_comb):
            if m <= len(curr_comb) <= n:
                self.res += 1
                # return            # 注意这里千万不要return, 因为加到m个number之后还可以往后再加的
                
            if len(curr_comb) >= n: # very strong pruning - after reach n points, we don't need to go to next
                return
            
            for next_num in nums:
                if next_num in visited:
                    continue
                if (curr_num, next_num) in cannot_pass and cannot_pass[(curr_num, next_num)] not in visited:
                    continue        # 这里是这题的题眼: No jumps through non selected key is allowed.
                visited.add(next_num)
                curr_comb.append(next_num)
                backtrack(next_num, curr_comb)
                curr_comb.pop()
                visited.remove(next_num)

        
        nums = [i for i in range(1, 10)]
        cannot_pass = {(1, 3): 2, (3, 1): 2, (1, 7): 4, (7, 1): 4, (3, 9): 6, (9, 3): 6, (7, 9): 8, (9, 7): 8,
                       (4, 6): 5, (6, 4): 5, (2, 8): 5, (8, 2): 5, (1, 9): 5, (9, 1): 5, (3, 7): 5, (7, 3): 5}
        
        self.res = 0
        # starts at 1, 3, 7, 9
        visited = set()
        visited.add(1)
        backtrack(1, [1])
        
        # starts at 2, 4, 6, 8
        visited = set()
        visited.add(2)
        backtrack(2, [2])
        
        self.res *= 4       # 利用对称性
        
        # starts at 5
        visited = set()
        visited.add(5)
        backtrack(5, [5])
        
        return self.res






class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        cannot_pass = {(1, 3): 2, (3, 1): 2, (1, 7): 4, (7, 1): 4, (3, 9): 6, (9, 3): 6, (7, 9): 8, (9, 7): 8,
                       (4, 6): 5, (6, 4): 5, (2, 8): 5, (8, 2): 5, (1, 9): 5, (9, 1): 5, (3, 7): 5, (7, 3): 5}
        
        
        def backtrack(curr_num, m, n, visited):
            if m <= len(visited) <= n:  # consider valid pattern only in range [m, n]
                self.ways += 1
            
            if len(visited) == n:       # after reach n points, we don't need to go to next
                return
            
            for next_num in range(1, 10):
                if next_num not in visited:
                    # if curr_num -> next_num has an obstacle and, and the obstacle is not visited previously, the cannot pass
                    if (curr_num, next_num) in cannot_pass and cannot_pass[(curr_num, next_num)] not in visited:
                        continue
                        
                    visited.add(next_num)
                    backtrack(next_num, m, n, visited)
                    visited.remove(next_num)
        
        self.ways = 0
        for num in range(1, 10):
            backtrack(num, m, n, {num})
            
        return self.ways
        
        
"""
利用对称性, 从1, 7, 3, 9出发的pattern数目是一样的，所以只需要计算从1出发的pattern数目再乘以4就可以了，同理2, 4, 6, 8
"""    
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        cannot_pass = {(1, 3): 2, (3, 1): 2, (1, 7): 4, (7, 1): 4, (3, 9): 6, (9, 3): 6, (7, 9): 8, (9, 7): 8,
                       (4, 6): 5, (6, 4): 5, (2, 8): 5, (8, 2): 5, (1, 9): 5, (9, 1): 5, (3, 7): 5, (7, 3): 5}
        
        
        def backtrack(curr_num, m, n, visited):
            if m <= len(visited) <= n:  # consider valid pattern only in range [m, n]
                self.ways += 1
            
            if len(visited) == n:       # after reach n points, we don't need to go to next
                return
            
            for next_num in range(1, 10):
                if next_num not in visited:
                    # if curr_num -> next_num has an obstacle and, and the obstacle is not visited previously, the cannot pass
                    if (curr_num, next_num) in cannot_pass and cannot_pass[(curr_num, next_num)] not in visited:
                        continue
                        
                    visited.add(next_num)
                    backtrack(next_num, m, n, visited)
                    visited.remove(next_num)
        
        self.ways = 0
        backtrack(1, m, n, {1})
        backtrack(4, m, n, {4})
        self.ways *= 4
        backtrack(5, m, n, {5})
            
        return self.ways
