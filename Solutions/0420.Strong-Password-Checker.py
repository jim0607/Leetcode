420. Strong Password Checker

A password is considered strong if below conditions are all met:

It has at least 6 characters and at most 20 characters.
It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.



"""
分三个区间讨论：
1. n <= 5: return max(6 - n, missing_types), 用三个小Helper function to calculate three missing_types;
2. 6 <= n <= 20: just need to return how many replacements are needed to avoid consecutive chars: 
number_of_replacements += num_of_consecutives // 3;
3. n > 20: step 1: calculate how many replacements are neededto avoid consecutive chars; 
step 2: calculate how many deletions can be used to save replacements - greedy.
"""
"""
class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        n = len(s)
        
        # missing types are how many types are missing in s
        missing_types = self._uppercase_check(s) + self._lowercase_check(s) + self._digit_check(s)

        if n <= 5:
            return max(6 - n, missing_types)

        # if n is in the acceptable range, then all the changes are replacements
        # we need to make replancements to avoid consecutive chars. eg: "aaaaaa" -> "aaBaa2"
        # the number that we need to make replacements are 6 // 3 = 2.
        # if there are types missing: eg: "abcdefg", we need at least replace to the missing type ->"abcdeF2"
        if 6 <= n <= 20:
            avoid_cons = 0          # how many replacements are needed to avoid consecutive chars
            consecutives = self._length_check(s)
            for num in consecutives:
                avoid_cons += num // 3      # eg: "aaaaaa" needs two replacement
            return max(avoid_cons, missing_types)
        
        # if n is too large, then we need to delete chars
        if n > 20:
            # step 1: calculate how many replacement are needed to avoid consecutive chars
            avoid_cons = 0          # how many replacements can be performed to avoid consecutive chars
            consecutives = self._length_check(s)
            for num in consecutives:
                avoid_cons += num // 3  
                
            # step 2: try save as much replacement as possible by deletion
            # "1AaaaaaaaaaKAKDFGHADF", there are 9 consecutive "a", and the lens of the password is 21 > 20.
            # we can choose to perform 9//3=3 replacement to avoid consecutive char, and 1 deletion to make the lens 20. 
            # Then overall, it will take 4 steps. However, if we also perform on the consecutive chars, that will be:
            # 8//3=2 for replacement and 1 for deletion, so 3 steps in total. See, we can save one replacement by deletion,
            # if 连续的chars的数目是3的倍数
            save_replacement = []      # how many deletions can be performed to save one replacment
            for num in consecutives:    
                save_replacement.append(num % 3 + 1)   # eg: if 连续的chars的数目是3的倍数, then we can perform 1 deletion to save 1 replacement
            save_replacement.sort()    # sort it so that the smallest number of deletions to save one replacement is in front
            
            # firstly, we do the cheap ones that takes only one deletion to save one replacement: - greedy
            # "aaa" -> "aa" is one deletion to save one replacement
            remain = n - 20     # how many deletions are remained make the password at most 20 chars
            for i in range(len(save_replacement)):
                if remain >= save_replacement[i]:    # make sure we have enough remaining to delete
                    remain -= save_replacement[i]    # deleted save_replacement[i] chars
                    avoid_cons -= 1                  # one replacement saved due to the deletion
                    
            # after the cheap ones, take the most expensive ones that takes two or three deletions to save one replacement
            # eg: "aaaa" -> "aa" two deletions save one replacement, "aaaaa" -> "aa" three deletions save one replacement
            avoid_cons -= remain // 3   # this might make avoid_cons negative, but it doesn't matter
            
            # step 3: update the res
            # remember, avoid_cons is number of replacement performed, 
            # if avoid_cons is too small (eg: 1), then we might miss missing_types in the password             
            return n - 20 + max(avoid_cons, missing_types)
            
        
    def _length_check(self, s):
        """
        take input as string "aaaaabbbbbbccdeee",
        and output a list of the cnt of chars that appears more than 3 times
        """
        consecutives = []
        curr_cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr_cnt += 1
            else:
                if curr_cnt >= 3:
                    consecutives.append(curr_cnt)
                curr_cnt = 1
        if curr_cnt >= 3:
            consecutives.append(curr_cnt)
        return consecutives
    
    
    def _uppercase_check(self, s):
        """
        return 1 if we need one uppercase
        """
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        upper = set(upper)
        for ch in s:
            if ch in upper:
                return 0
        return 1
    
    
    def _lowercase_check(self, s):
        """
        return 1 if we need one lowercase
        """
        lower = "abcdefghijklmnopqrstuvwxyz"
        lower = set(lower)
        for ch in s:
            if ch in lower:
                return 0
        return 1
    
    
    def _digit_check(self, s):
        """
        return 1 if we need one digit
        """
        digits = "0123456789"
        digits = set(digits)
        for ch in s:
            if ch in digits:
                return 0
        return 1
