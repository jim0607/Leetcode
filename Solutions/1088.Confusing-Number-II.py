"""
1088. Confusing Number II

We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.

A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.)

Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.

Example 1:

Input: 20
Output: 6
Explanation: 
The confusing numbers are [6,9,10,16,18,19].
6 converts to 9.
9 converts to 6.
10 converts to 01 which is just 1.
16 converts to 91.
18 converts to 81.
19 converts to 61.
Example 2:

Input: 100
Output: 19
Explanation: 
The confusing numbers are [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].
"""

"""
time complexity: O(M*5^M)
"""
class Solution:
    def confusingNumberII(self, N: int) -> int:
        def backtrack(curr_comb):
            if int(curr_comb) > N:
                return
            
            if is_confusing(curr_comb):
                res.add(curr_comb)      # 注意这里不要return, 因为"16"是valid的，"168"也是valid的
                
            for num in mapping:
                backtrack(curr_comb + num)
                
        
        def is_confusing(comb):
            rotated = ""
            for i in range(len(comb) - 1, -1, -1):
                rotated += mapping[comb[i]]
            return rotated != comb
        
        
        nums = ["1", "6", "8", "9"]
        mapping = {"0": "0", "1": "1", "6": "9", "9": "6", "8": "8"}
        res = set()
        for num in nums:
            backtrack(num)
        return len(res)








"""
solution 1: brutal force with memo - TLE
"""
class Solution:
    def confusingNumberII(self, N: int) -> int:
        cnt = 0
        memo = set()        # store all the already found confusing number
        for num in range(1, N+1):
            if num in memo:
                cnt += 1
                continue
                
            confusing, rotated = self._confusingNumber(num)
            if confusing:
                memo.add(num)
                memo.add(rotated)
                cnt += 1
                
        return cnt        
        
    def _confusingNumber(self, N: int) -> (bool, int):
        mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        s = str(N)
        if any(ch for ch in s if ch not in mapping): return False, -1
        rotated = ""
        for i in range(len(s) - 1, -1, -1):
            rotated += mapping[s[i]]
        return rotated != s, int(rotated)
        
        
        
"""
solution 2: Only 0, 1, 6, 8, 9 are the valid set of digits, do a backtracking to generate all the numbers containing this digits and check they are valid.
time complexity: O(5^M), where M is how many digits are there in str(N), which scales with ~logN, where log is 10-based.
"""
class Solution:
    def confusingNumberII(self, N: int) -> int:
        def backtrack(curr_num, curr_rotated):
            if int(curr_num) > N:
                return
            
            if curr_num != curr_rotated:
                self.cnt += 1
                
            for ch in mapping:
                next_num = curr_num + ch
                next_rotated = mapping[ch] + curr_rotated    # 注意加的顺序
                backtrack(next_num, next_rotated)   # 都是immutable的数据结构，不需要后面的remove或pop部分了

                
        self.cnt = 0
        mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        for num in ["1", "6", "8", "9"]:    # 这里是初始化bachtrack的其实参数，这里不要把"0"加进去，因为"0"不能作为一个数的开头
            backtrack(num, mapping[num])        
        return self.cnt
