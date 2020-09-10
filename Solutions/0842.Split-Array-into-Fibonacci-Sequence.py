"""
842. Split Array into Fibonacci Sequence

Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
"""


"""
套backtrack模板即可，backtrack传入的参数有(curr_idx, curr_comb). 
结束条件是if curr_idx == len(s) - 1 and len(curr_comb) > 2:
"""
class Solution:
    def splitIntoFibonacci(self, s: str) -> List[int]:
        def backtrack(curr_idx, curr_comb):
            if curr_idx == len(s) - 1 and len(curr_comb) > 2:
                res.append(curr_comb.copy())
                return
            for next_idx in range(curr_idx + 1, len(s)):
                if s[curr_idx + 1] == "0" and next_idx != curr_idx + 1: # 0 is a valid number but 01 is not
                    continue
                next_num = int(s[curr_idx + 1: next_idx + 1])
                if next_num > 2**31 - 1:        # 题目要求0 <= F[i] <= 2^31 - 1
                    continue
                if len(curr_comb) <= 1:
                    curr_comb.append(next_num)
                    backtrack(next_idx, curr_comb)
                    curr_comb.pop()
                elif len(curr_comb) >= 2:
                    if next_num == curr_comb[-1] + curr_comb[-2]:
                        curr_comb.append(next_num)
                        backtrack(next_idx, curr_comb)
                        curr_comb.pop()

                    
        res = []
        backtrack(-1, [])
        return res[0] if len(res) > 0 else []





"""
与上一题相比要求输出所有Fibonacci组合，所以用backtrack: pass curr as signature to record the curr path/res
"""
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        self.res = []
        for first_idx in range(len(num) - 2):
            if num[0] == "0" and first_idx > 0:       # 0 is a valid number but 01 is not
                    continue
            first_num = int(num[:first_idx+1])
            if first_num > 2**31 - 1:           # 题目要求0 <= F[i] <= 2^31 - 1
                continue
            for second_idx in range(first_idx + 1, len(num) - 1):
                if num[first_idx+1] == "0" and second_idx > first_idx + 1:       # 0 is a valid number but 01 is not
                    continue
                second_num = int(num[first_idx+1:second_idx+1])
                if second_num > 2**31 - 1:
                    continue
                self._dfs(num, first_num, first_idx, second_num, second_idx, [first_num, second_num])
                          
        return self.res[0] if self.res else []      # res里面包含了所有的可能结果
    
    def _dfs(self, num, prev_num, prev_idx, curr_num, curr_idx, curr):
        if curr_idx == len(num) - 1:
            self.res.append(curr.copy())
            return
        
        for next_idx in range(curr_idx + 1, len(num)):
            if num[curr_idx+1] == "0" and next_idx > curr_idx + 1:
                continue
            next_num = int(num[curr_idx+1:next_idx+1])
            if next_num > 2**31 - 1:
                continue
            if next_num == prev_num + curr_num:
                curr.append(next_num)
                self._dfs(num, curr_num, curr_idx, next_num, next_idx, curr)
                curr.pop()
                
        return False
