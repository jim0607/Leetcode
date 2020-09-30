"""
1044. Longest Duplicate Substring

Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

Example 1:

Input: "banana"
Output: "ana"
Example 2:

Input: "abcd"
Output: ""

Note:
2 <= S.length <= 10^5
S consists of lowercase English letters.
"""



"""
step 1: find the lens of longest duplicated substring using binary search - 1062. Longest Repeating Substring;
step 2: use the longest lens to find the substring - 187. Repeated DNA Sequences
"""
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        L = self.longestRepeatingSubstring(s)       # step 1: find the lens of longest duplicated substring using binary search  
        return self.findRepeatedDnaSequences(s, L)  # step 2: use the longest lens to find the substring
        
    # below is just a copy of 1062. Longest Repeating Substring
    def longestRepeatingSubstring(self, s: str) -> int:
        start, end = 0, len(s) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._has_repeat(s, mid):
                start = mid
            else:
                end = mid
        return end if self._has_repeat(s, end) else start
    
    def _has_repeat(self, s, L):
        """
        Return if there are two L-long substrings that are equal
        """
        SIZE = 2**31        # 由于采用了冲突解决办法，所以size选的很小也没关系
        BASE = 31
        power = 1
        for _ in range(L):
            power = (power * BASE) % SIZE
            
        mapping = collections.defaultdict(set)      # hash_code --> strings with that hash_code
        hash_code = 0
        for i, ch in enumerate(s):
            hash_code = (hash_code * BASE + ord(ch) - ord("a")) % SIZE
            if i < L - 1:
                continue
            if i >= L:
                hash_code = (hash_code - (ord(s[i-L]) - ord("a")) * power % SIZE) % SIZE    # ***注意每一步都要 % SIZE, 防止数字越界,
            if hash_code in mapping:                      # 这样写有两个case过不了hash_code -= (ord(s[i-L]) - ord("a")) * power % SIZE
                if s[i-L+1:i+1] in mapping[hash_code]:
                    return True
            mapping[hash_code].add(s[i-L+1:i+1])
        return False
    
    # below is just a copy of 187. Repeated DNA Sequences
    def findRepeatedDnaSequences(self, s: str, L: int) -> List[str]:
        HASH_SIZE = 2**31
        BASE = 31  

        power = 1
        for _ in range(L):
            power = power * BASE % HASH_SIZE
            
        hash_code = 0
        hash_code_set = set()
        for i, ch in enumerate(s):
            hash_code = (hash_code * BASE + ord(ch) - ord("a")) % HASH_SIZE
            if i < L - 1:
                continue
            if i >= L:
                hash_code = (hash_code - (ord(s[i-L]) - ord("a")) * power % HASH_SIZE) % HASH_SIZE
            
            if hash_code in hash_code_set:
                return s[i-L+1: i+1]
            hash_code_set.add(hash_code)
