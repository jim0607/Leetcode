"""
291. Word Pattern II

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Example 1:

Input: pattern = "abab", str = "redblueredblue"
Output: true
Example 2:

Input: pattern = "aaaa", str = "asdasdasdasd"
Output: true
Example 3:

Input: pattern = "aabb", str = "xyzabcxzyabc"
Output: false
 

Constraints:

You may assume both pattern and str contains only lowercase letters.
"""



"""
backtrack传入参数(curr_s_idx, curr_p_idx, ch_to_str, str_to_ch).
backtrack结束条件: if curr_s_idx == len(s) - 1 and curr_p_idx == len(pattern) - 1.
is valid: if ch_to_str[next_ch] == next_word and str_to_ch[next_word] == next_ch.
"""
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backtrack(curr_s_idx, curr_p_idx, ch_to_str, str_to_ch):
            if curr_s_idx == len(s) - 1 and curr_p_idx == len(pattern) - 1:
                return True
            if curr_s_idx == len(s) - 1:
                return False
            if curr_p_idx == len(pattern) - 1:
                return False
            for next_s_idx in range(curr_s_idx + 1, len(s)):
                next_ch = pattern[curr_p_idx + 1]
                next_word = s[curr_s_idx + 1: next_s_idx + 1]
                if next_ch in ch_to_str:
                    if ch_to_str[next_ch] != next_word or str_to_ch[next_word] != next_ch:
                        continue
                    if backtrack(next_s_idx, curr_p_idx + 1, ch_to_str, str_to_ch):
                        return True
                else:
                    if next_word in str_to_ch:
                        continue
                    ch_to_str[next_ch] = next_word
                    str_to_ch[next_word] = next_ch
                    if backtrack(next_s_idx, curr_p_idx + 1, ch_to_str, str_to_ch):
                        return True
                    del ch_to_str[next_ch]      # 这里的del相当于visited.remove - 做backtrack
                    del str_to_ch[next_word]
            return False
                    
                
        ch_to_str = collections.defaultdict(str)
        str_to_ch = collections.defaultdict(str)
        return backtrack(-1, -1, ch_to_str, str_to_ch)

""" 只要熟练理解背诵backtrack模板, 再难的题也是一遍过 """








"""
backtracking solution.  next candidate is valid only if string[curr_idx:next_idx] is satisfy the mapping condition.
"""
class Solution:
    def wordPatternMatch(self, pattern: str, words: str) -> bool:
        lens = len(words)
        if lens < len(pattern):
            return False

        self.flag = False
        
        def backtrack(curr_idx, curr_cut, mapping):
            if curr_idx == lens and curr_cut == len(pattern):
                self.flag = True
                return
            
            if curr_idx >= lens or curr_cut >= len(pattern):
                return
            
            for next_idx in range(curr_idx + 1, lens + 1):
                next_str = words[curr_idx:next_idx]
                
                if next_str in mapping.values() and pattern[curr_cut] in mapping and next_str == mapping[pattern[curr_cut]]:
                    backtrack(next_idx, curr_cut + 1, mapping)      # 这里不做backtracking因为并没有把pattern[curr_cut]放到mapping里，mapping里原来就有pattern[curr_cut]
                
                elif next_str not in mapping.values():
                    if pattern[curr_cut] in mapping.keys():
                        continue
                    mapping[pattern[curr_cut]] = next_str
                    backtrack(next_idx, curr_cut + 1, mapping)
                    del mapping[pattern[curr_cut]]      # backtracking

        mapping = collections.defaultdict()
        backtrack(0, 0, mapping)    

        return self.flag
