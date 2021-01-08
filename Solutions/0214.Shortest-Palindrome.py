"""
214. Shortest Palindrome

Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. 
Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
"""




"""
The problem really is to find the longest palindrome starts with s[0].
rabin carp / rolling hash O(N). The algorithm is for string s, left_code = the hash_code scan from left to right,
right_code = the hash_code scan from right to left. if left_code == right_code, then s is a palindrome.
"""
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        lens = self.longest_palind(s)
        pre = s[lens:]
        return pre[::-1] + s
        
    def longest_palind(self, s):    # returns the longest palindrome starts with s[0]
        hash_size = 10**9 + 7
        power = 1
        left_code, right_code = 0, 0
        lens = 1
        for i, ch in enumerate(s):
            left_code = (left_code * 31 + ord(ch) - ord("a")) % hash_size           # 从左至右扫的hash_code
            right_code = (power * (ord(ch) - ord("a")) + right_code) % hash_size    # 从右往左扫的hash_code
            power = 31 * power % hash_size
            
            if left_code == right_code:
                lens = i + 1
        return lens



"""
find the longest palindrome start with s[0].
O(N^2). passed 119/120 cases.
"""
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s or len(s) <= 1:
            return s
        
        # step 1: first store the all the idx that equals s[0]
        idx_lst = []
        for idx, ch in enumerate(s):
            if ch == s[0]:
                idx_lst.append(idx)

        # step 2: then find the longest palindrome start with s[0]
        n = len(s)
        palin_idx = 0
        for idx in idx_lst[::-1]:   # 注意这里只能Linear search不能binary search, 因为drop half是不行的
            if self._is_palin(s, 0, idx):
                palin_idx = idx
                break
        
        return s[palin_idx + 1:][::-1] + s
    
    def _is_palin(self, s, start, end):
        i, j = start, end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
