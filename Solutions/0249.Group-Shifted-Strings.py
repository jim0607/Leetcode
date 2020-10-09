"""
249. Group Shifted Strings

Given a string, we can "shift" each of its letter to its successive letter, 
for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets, 
group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""


"""
hashmap. similar with 49. Group Anagrams.
the key of the hashmap is a tuple of the list [ord(ch)-ord(first_ch) for ch in each string]
"""
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        str_dict = collections.defaultdict(list)
        for s in strings:
            ch_lst = []
            for ch in s:
                ch_lst.append((ord(ch) - ord(s[0])) % 26)   # "za"会形成环，所以take mod of 26
            str_dict[tuple(ch_lst)].append(s)
        
        return str_dict.values()
