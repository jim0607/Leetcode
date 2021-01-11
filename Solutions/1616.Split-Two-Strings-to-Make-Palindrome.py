"""
1616. Split Two Strings to Make Palindrome

You are given two strings a and b of the same length. Choose an index and split both strings at the same index, 
splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. 
Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.

When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. 
For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.

Return true if it is possible to form a palindrome string, otherwise return false.

Notice that x + y denotes the concatenation of strings x and y.

Example 1:

Input: a = "x", b = "y"
Output: true
Explaination: If either a or b are palindromes the answer is true since you can split in the following way:
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.
Example 2:

Input: a = "abdef", b = "fecab"
Output: true
Example 3:

Input: a = "ulacfd", b = "jizalu"
Output: true
Explaination: Split them at index 3:
aprefix = "ula", asuffix = "cfd"
bprefix = "jiz", bsuffix = "alu"
Then, aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.
Example 4:

Input: a = "xbdef", b = "xecab"
Output: false
 
Constraints:

1 <= a.length, b.length <= 105
a.length == b.length
a and b consist of lowercase English letters
"""


"""
Greedily take the a_suffix and b_prefix as long as they are palindrome,
that is, a_suffix = reversed(b_prefix).
The the middle part of a is s1,
The the middle part of b is s2.
If either s1 or s2 is palindrome, then return true.

Time O(N), Space O(N)
"""
class Solution:
    def checkPalindromeFormation(self, s: str, t: str) -> bool:
        if self.is_palin(s) or self.is_palin(t):
            return True
        
        middle = []
        n = len(s)
        i, j = 0, n - 1
        while i < n:
            if s[i] != t[j]:
                break
            i += 1
            j -= 1
        middle.append(s[i:j+1])
        middle.append(t[i:j+1])
        
        i, j = n - 1, 0
        while j < n:
            if s[i] != t[j]:
                break
            i -= 1
            j += 1
        middle.append(s[j:i+1])
        middle.append(t[j:i+1])
        
        for substr in middle:
            if self.is_palin(substr):
                return True
        return False
        
        
    def is_palin(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        
"""
O(n^2) solution
"""
class Solution:
    def checkPalindromeFormation(self, s: str, t: str) -> bool:
        if self.is_palin(s) or self.is_palin(t):
            return True
        
        n = len(s)
        for i in range(n+1):
            pre_s = s[:i]
            suf_s = s[i:]
            pre_t = t[:i]
            suf_t = t[i:]
            if self.is_palin(pre_s + suf_t) or self.is_palin(pre_t + suf_s):
                return True
        return False
    
        
    def is_palin(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
