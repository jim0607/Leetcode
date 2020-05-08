139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false


"""
dp[i]=can partition until ith char?, not including i
dp[j]=true if (for i < j, there is dp[i]=True and s[i:j]is in wordDict)
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lens = len(s)
        wordSet = set()
        for word in wordDict:
            wordSet.add(word)
            
        dp = [False for _ in range(lens + 1)]
        dp[0] = True
        
        for j in range(1, lens + 1):
            for i in range(j):   # 这句话应该改成for i in range(j-1,-1,-1), 因为从 s[i:j] in wordSet 就更容易判断更快了！
                if dp[i] and s[i:j] in wordSet:     # 这句话应该把dp[i]==True放到前面，因为dp[i]==True is low cost comparison.
                    dp[j] = True
                    break
                    
        return dp[lens]
