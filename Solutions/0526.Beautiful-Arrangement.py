526. Beautiful Arrangement

Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
 

Now given N, how many beautiful arrangements can you construct?

Example 1:

Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.


"""
For permutation problem, the 1st idx has N choices of number, 2nd has n-1 choices.
so time complexity id O(solutions = N!). 
For constrained permutation problem, the time complexity is O(valid solutions)
下面的解法会 TLE
"""
class Solution:
    def countArrangement(self, N: int) -> int:
        self.res = 0
        used_nums = set()
        self._backtrack(N, 0, used_nums)
        return self.res
    
    def _backtrack(self, N, curr_pos, used_nums):
        if curr_pos == N and len(used_nums) == N:
            self.res += 1
            return 
        
        for pos in range(curr_pos + 1, N + 1):
            for num in range(1, N+1):
                if num in used_nums:
                    continue
                if num % pos != 0 and pos % num != 0:
                    continue
                used_nums.add(num)
                self._backtrack(N, pos, used_nums)
                used_nums.remove(num)
                
                
"""
下面这个解法就快多了
"""             
class Solution:
    def countArrangement(self, N: int) -> int:
        self.res = 0
        used_nums = set()
        self._backtrack(N, 1, used_nums)
        return self.res
    
    def _backtrack(self, N, curr_pos, used_nums):
        if curr_pos > N:
            self.res += 1
            return 
        # 从1 - N+1中选一个数字放入到curr_pos上
        for num in range(1, N + 1):
            if num in used_nums:
                continue
            if num % curr_pos != 0 and curr_pos % num != 0:
                continue
            used_nums.add(num)
            self._backtrack(N, curr_pos + 1, used_nums)
            used_nums.remove(num)
