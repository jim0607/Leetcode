"""
1048. Longest String Chain

Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  
For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.


Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
 

Note:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
"""


"""
dp = dict, key is word, val is the longest chain lens ended with word
predecessor = word[:i]+word[i+1:]
if predecessor in dp: dp[word] = max(dp[redesessor]+1)
O(MN)
"""
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x: len(x))      # sort by lens of word
        
        # key is word, val is the LSC ended with the word
        dp = defaultdict(lambda: 1)
        max_lens = 0
        for word in words:              # O(N)
            for i in range(len(word)):  # O(M), where M is length of word
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
                    
            max_lens = max(max_lens, dp[word])
            
        return max_lens

       
"""
similar with 300. Longest Increasing Subsequence - O(MN^2)
"""
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x: len(x))      # sort by lens of word
        
        dp = [1 for _ in range(len(words))]
        for j in range(1, len(words)):
            for i in range(j - 1, -1, -1):
                if len(words[i]) + 1 == len(words[j]):
                    if self.is_valid(words[i], words[j]):
                        dp[j] = max(dp[j], dp[i] + 1)
                
                elif len(words[i]) + 1 < len(words[j]):
                    break
                    
        return max(dp)
    
    def is_valid(self, s, t):
        for i in range(len(t)):
            if s == t[:i] + t[i+1:]:
                return True
        return False
       
       
       
       

"""
注意用word ladder类似的bfs是解不了的，因为最长的那个chain不一定是从minLens word开始的，所以根本不知道第一步哪些word append到queue里。
"""
