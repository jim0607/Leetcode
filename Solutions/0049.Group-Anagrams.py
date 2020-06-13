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


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key is a tuple keeping track of the cnt of all 26 letters
        # val is the word list corresponding to the tuple
        wordsDict = collections.defaultdict(list)
        for word in strs:
            cnt = [0 for _ in range(26)]
            for ch in word:
                cnt[ord(ch)-ord("a")] += 1
            wordsDict[tuple(cnt)].append(word)     # need to change cnt to a tuple because list is unhashable due ot list is mutable
            
        return wordsDict.values()
