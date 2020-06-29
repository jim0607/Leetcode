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


class Solution:
    def wordPattern(self, pattern: str, words_str: str) -> bool:
        words = []
        i = 0
        while i < len(words_str):
            anchor = i
            while i < len(words_str) and words_str[i] != " ":
                i += 1
            words.append(words_str[anchor:i])  
            i += 1
            
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
