"""
616. Add Bold Tag in String

Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. 
If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. 
Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:

Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
 
Example 2:

Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
"""


class Solution:
    def addBoldTag(self, s: str, lst: List[str]) -> str:
        # step 1: store the (start_idx, end_idx) for every appearance of substring in s
        # Algorithm: 28. Implement strStr() Rabin Karp - O((M+N)*W) 
        # where N is len(s), M is avg lens of words in dict, and W is len(dict)
        intervals = []
        for substr in lst:
            intervals += self.strStr(s, substr)

        # step 2: now we have a list of (start, end) intervals, we merge interval 
        # so that we don't have overlaps anymore.  Algorithm: 56. merge intervals
        intervals = self.merge(intervals)

        # step 3: add <b> and </b> pair to generate res
        res = ""
        i, j = 0, 0
        while i < len(intervals) and j < len(s):
            start, end = intervals[i]
            if j < start:
                res += s[j]
                j += 1
            elif j == start:
                res += "<b>" + s[j:end] + "</b>"
                i += 1
                j = end
        while j < len(s):       # 如果最后还有
            res += s[j]
            j += 1
        return res        
        
    def strStr(self, source: str, target: str) -> int:
        """
        Return the index of the first occurrence of needle in haystack, 
        or -1 if needle is not part of haystack. 
        """
        n, m = len(source), len(target)
        SIZE = 2**31
        BASE = 31
        res = []
        
        # step 1: calculate the hash code for target
        target_code = 0
        for ch in target:
            target_code = (target_code * 31 + (ord(ch) - ord("a"))) % SIZE
            
        # step 2: calculate the hash code for source in a sliding window
        power = 1       # get the power so that we can substract in the source_code
        for _ in range(m):      
            power = power * 31 % SIZE
            
        source_code = 0
        for i, ch in enumerate(source):
            source_code = (source_code * 31 + (ord(ch) - ord("a"))) % SIZE
            if i >= m:       # maintain a m-size window
                source_code = (source_code - (ord(source[i-m]) - ord("a")) * power) % SIZE  
            if i >= m - 1 and source_code == target_code:
                res.append([i - m + 1, i - m + 1 + m])
        return res
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        
        intervals.sort(key = lambda x: (x[0], x[1]))
        
        merged = [intervals[0]]
        for interval in intervals:
            if interval[0] > merged[-1][1]:  # if the interval start time is larger than the largest end time in merged
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
