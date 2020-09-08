"""
290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""



"""
similar with 1153. String Transforms Into Another Strin. use a mapping to map ch to str, 
and use another mapping to map str to ch.
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = s.split(" ")
        if len(pattern) != len(lst):
            return False
        
        ch_to_str = collections.defaultdict(str)
        str_to_ch = collections.defaultdict(str)
        for i in range(len(lst)):
            ch = pattern[i]
            word = lst[i]
            if ch in ch_to_str:
                if ch_to_str[ch] != word or str_to_ch[word] != ch:
                    return False
            else:
                if word in str_to_ch:
                    return False
                ch_to_str[ch] = word
                str_to_ch[word] = ch
                
        return True
    



"""
The following takes O(N^2) using one hashmap
"""
class Solution:
    def wordPattern(self, pattern: str, words_str: str) -> bool:
        words = words_str.split(" ")
            
        lens = len(pattern)
        if len(words) != lens:
            return False
        
        mapping = collections.defaultdict()
        for i, ch in enumerate(pattern):
            if ch in mapping:
                if mapping[ch] != words[i]:
                    return False
            else:
                if words[i] in mapping.values():        # to pass this case: "abba", "dog dog dog dog"
                    return False
                mapping[ch] = words[i]
                
        return True
