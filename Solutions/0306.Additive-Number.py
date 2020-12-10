"""
306. Additive Number

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. 
Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
"""
            

   
"""
套backtrack模板即可
end condition is next_idx == len(s) - 1.
constraint is: 1. not leading zero; 2. has to equal to the prev two num add together.
backtrack function pass: (curr_idx, curr_comb)
backtrack function should return whether or not it is valid
"""
class Solution:
    def isAdditiveNumber(self, s: str) -> bool:
        def backtrack(curr_idx, curr_comb):
            if curr_idx == len(s) - 1 and len(curr_comb) >= 3:
                return True
            
            for next_idx in range(curr_idx + 1, len(s)):
                next_num = s[curr_idx + 1 : next_idx + 1]
                if next_num[0] == "0" and len(next_num) > 1:        # no leading zero
                    continue
                if len(curr_comb) < 2 or (len(curr_comb) >= 2 and int(next_num) == int(curr_comb[-1]) + int(curr_comb[-2])):
                    curr_comb.append(next_num)
                    if backtrack(next_idx, curr_comb):
                        return True
                    curr_comb.remove(next_num)
            return False
        
        
        return backtrack(-1, [])
   
   
   


"""
自己写的dfs, easy to understand
"""
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for first_idx in range(len(num) - 2):
            if num[0] == "0" and first_idx > 0:       # 0 is a valid number but 01 is not
                    continue
            for second_idx in range(first_idx + 1, len(num) - 1):
                if num[first_idx+1] == "0" and second_idx > first_idx + 1:       # 0 is a valid number but 01 is not
                    continue
                if self._dfs(num, int(num[:first_idx+1]), first_idx, int(num[first_idx+1:second_idx+1]), second_idx):
                    return True
        return False
    
    def _dfs(self, num, prev_num, prev_idx, curr_num, curr_idx):
        if curr_idx == len(num) - 1:
            return True
        
        for next_idx in range(curr_idx + 1, len(num)):
            if num[curr_idx+1] == "0" and next_idx > curr_idx + 1:
                continue
            next_num = int(num[curr_idx+1:next_idx+1])
            if next_num == prev_num + curr_num:
                if self._dfs(num, curr_num, curr_idx, next_num, next_idx):
                    return True
                
        return False
