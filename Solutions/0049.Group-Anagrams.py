"""
49. Group Anagrams

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = collections.defaultdict(list)
        for word in strs:
            ch_to_cnt = [0 for _ in range(26)]  # 正发愁用什么最为dictionary的key, 这样定义counter真的很巧妙, 然后转换成tuple真得很巧妙
            for ch in word:
                ch_to_cnt[ord(ch) - ord("a")] += 1
                
            word_dict[tuple(ch_to_cnt)].append(word)    # need to change cnt to a tuple because list is unhashable due ot list is mutable
            
        return word_dict.values()
