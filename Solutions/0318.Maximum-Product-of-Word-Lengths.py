318. Maximum Product of Word Lengths

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.


"""
O(NlogN + N^2*L)
"""
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words = sorted(words, key = lambda x: -len(x))
        max_prod = 0
        for i, word in enumerate(words):
            w_set = set(word)
            for j in range(i+1, len(words)):
                valid = True
                for char in words[j]:
                    if char in w_set:
                        valid = False
                        break
                if valid: 
                    max_prod = max(max_prod, len(words[j]) * len(word))
                    
        return max_prod
