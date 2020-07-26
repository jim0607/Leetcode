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
time complexity: O(L*(number of solutions)), where L is avg lens used to check is_confusingNumber.
"""
class Solution:
    def confusingNumberII(self, N: int) -> int:
        valid_lst = ["0", "1", "6", "8", "9"]
        self.cnt = 0
        included = set()
        self._backtrack(N, valid_lst, "", included)
        return self.cnt
    
    def _backtrack(self, N, valid_lst, curr_num, included):
        if curr_num and int(curr_num) <= N and self._is_confusingNumber(curr_num):
            self.cnt += 1       # 注意不能return，因为"66"后面还可以再加eg:"661", "668"等等
            
        if curr_num and int(curr_num) > N:
            return        # 注意不能写成continue, continue只能用在loop里，所以这里写return相当于continue
        
        if curr_num and curr_num[0] == "0":     # 注意0开头的数字无效
            return
        
        for ch in valid_lst:
            next_num = curr_num + ch
            if next_num in included:
                continue
            included.add(next_num)
            self._backtrack(N, valid_lst, next_num, included)
            included.remove(next_num)
                
    def _is_confusingNumber(self, s) -> (bool, int):
        mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        rotated = ""
        for i in range(len(s) - 1, -1, -1):
            rotated += mapping[s[i]]
        return rotated != s
