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
Need to find a path, so backtracking.  O(2^m + m^2 + n), where m is the lens of string, n is the lens of word_dict.
O(2^m) comes from backtracking on the string, cuz each 每个ch之间我们可以选择切一刀或不切一刀.
O(m^2) comes from the checking for wordBreakI.  O(n) for converting word_dict to a set.
"""
class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> List[str]:
        word_set = set()
        for word in word_dict:
            word_set.add(word)
 
        lens = len(s)
        res = []
    
        # if cannot make it, then we don't need to find a path.  This ckeck makes it from TLE to 90%
        if not self.wordBreakI(s, word_set):      
            return []
        
        def backtrack(curr_idx, curr_path):
            if curr_idx == lens:
                res.append(curr_path)
                return
                
            for i in range(curr_idx + 1, lens + 1):
                next_word = s[curr_idx:i]
                if next_word in word_set:
                    if curr_path:
                        backtrack(i, curr_path + " " + next_word)
                    else:
                        backtrack(i, next_word)     # 第一个单词前不需要空格" ", 这种需要输出特殊格式的题目往往都需要吧第一次访问单独列出来， eg: LC 282
                    
        backtrack(0, "")
        
        return res
    
    
    # Below I just copied the solution from 139. Word Break I
    def wordBreakI(self, s: str, word_set: List[str]) -> bool:
        lens = len(s)
        memo = collections.defaultdict()

        def dfs(curr_idx):
            if curr_idx == lens:
                return True

            if curr_idx in memo:
                return memo[curr_idx]

            for i in range(curr_idx + 1, lens + 1):
                next_word = s[curr_idx:i]
                if next_word in word_set:
                    if dfs(i):
                        memo[curr_idx] = True
                        return True

            memo[curr_idx] = False
            return memo[curr_idx]

        return dfs(0)
