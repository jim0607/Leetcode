"""
1062. Longest Repeating Substring

Given a string S, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.

Example 1:

Input: "abcd"
Output: 0
Explanation: There is no repeating substring.
Example 2:

Input: "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
Example 3:

Input: "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.
Example 4:

Input: "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.
"""

"""
solution 1: binary search
"""
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:     # O(NLlogN)
        start, end = 0, len(s)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.exist(s, mid):
                start = mid
            else:
                end = mid
        return end if self.exist(s, end) else start
    
    def exist(self, s, L):      # O(NL)
        """
        return if there exists L-lens repeating string in s
        """
        sub_s = deque()
        sub_s_set = set()
        for i, ch in enumerate(s):
            sub_s.append(ch)
            if i >= L:
                sub_s.popleft()
            
            if i >= L - 1:
                if str(sub_s) in sub_s_set:
                    return True
                sub_s_set.add(str(sub_s))
                
        return False                


"""
可以从lens-1开始逐个去试，takes O(N^2). 也可以用binary search去试.
如果存在repeating substring的长度是L的话，那么也一定存在repeating substring的长度是小于L的;
所以主体是一个OOXXX问题，寻找first L to satisfy that there are two substring both L long and equal.
确定了是binary search之后就来思考怎样drop左边或者右边，如果不存在two substring both mid long and equal, 那就drop right;
如何快速判断是否存在two substring with length = mid that equal? 
Using rolling hash to check if two substring have the same hash_code, using rolling hash, we realized O(1) string comparison;
So the overall time complexity is O(nlogn), where n is the lens of S
"""

class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        lens = len(S)
        start, end = 0, lens - 1
        while start + 1 < end:
            mid = start + (end - start ) // 2
            if self.exist_repeating_substring(S, mid):
                start = mid
            else:
                end = mid
        
        return end if self.exist_repeating_substring(S, end) else start
    
    def exist_repeating_substring(self, S, L):    
        """
        return a boolean: whether of not there are two equal substring that are L long
        """
        HASH_SIZE = 2 ** 31         # hash_size如果选10**7这题就过不了，因为有很多冲突导致exist_repeating_substring很容易有错误的输出
        power = 1
        for _ in range(L):
            power = (power * 31) % HASH_SIZE
        
        hash_code = 0
        hash_code_set = set()
        for i, ch in enumerate(S):
            hash_code = (hash_code * 31 + (ord(ch) - ord("a"))) % HASH_SIZE
            if i < L - 1:
                continue
            if i >= L:
                hash_code = (hash_code - (ord(S[i - L]) - ord("a")) * power % HASH_SIZE) % HASH_SIZE
            if hash_code in hash_code_set:      
                return True
            hash_code_set.add(hash_code)
            
        return False 

    
    
    
    
"""
冲突解决办法： 如果hash_code相等，我们还需要再check string是否相等
"""
class Solution:
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
        SIZE = 2**10        # 由于采用了冲突解决办法，所以size选的很小也没关系
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
