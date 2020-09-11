"""
140. Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""


"""
Need to find a path, so backtracking.  O(2^m + m^2 + n), where m is the lens of string, n is the lens of word_dict.
O(2^m) comes from backtracking on the string, cuz each 每个ch之间我们可以选择切一刀或不切一刀.
O(m^2) comes from the checking for wordBreakI.  O(n) for converting word_dict to a set.
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:       
        def backtrack(curr_idx, curr_path):     # 套用backtrack模板即可
            if curr_idx == len(s) - 1:
                res.append(curr_path[1:])
                return
            for next_idx in range(curr_idx + 1, len(s)):
                next_word = s[curr_idx + 1: next_idx + 1]
                if next_word in word_set:
                    backtrack(next_idx, curr_path + " " + next_word)

            
        word_set = set(wordDict)
        if not self._wordBreak(s, word_set):  # This ckeck makes it from TLE to 90%, cuz it only takes O(N^2) 
            return []                         # if cannot make it, then we don't need to find a path.
        
        res = []
        backtrack(-1, "")
        return res
    
    def _wordBreak(self, s, word_set) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for j in range(len(dp)):
            for i in range(j-1, -1, -1):
                if dp[i] and s[i:j] in word_set:
                    dp[j] = True
                    break
        return dp[-1]
