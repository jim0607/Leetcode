336. Palindrome Pairs

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]


"""
https://www.youtube.com/watch?v=XpxCzLl61lU
There are 2 cases for the possibility of word1 and word2 to form a palindrome:
case 1: len(word1)==len(word2) eg: "abc", "cba", in this case, it is very easy to check if word1 and word2 are palindrome;
case 2: len(word1)>len(word2) 
in this case, there are two possibilities that word1 and word2 can form a palindrome.  
possibility 1: word1 + word2.  eg: "racece", "car", we first remove the last word (the suffix) "e" of word1 and get "racec". 
Then we check two conditions: 1. is the removed word "e" a palindrome? 2. is the remaining word1 "racec" and word2 "car" a palindrome "raceccar"? 
if both conditions satisfied, then yes, word1 and word2 can be palindrome. 
If not, let's keep removing the last word "ce" and get "race", we check again and find that "racecar" is indeed a palindrom,
but "ce" is not. so we keep removing the last word "ece" and check again and find that "raccar" is indeed a palindrome and "ece" is also a palindrome, 
so word1 + word2 is a palindrom.
possibility 2: word2 + word1.  eg: "rarun", "nu".  in this case we do the same thing as possibility 1 except 
we remove the front (the prefix) of the word1, until the front "rar" is a palindrome and "un" + "nu" is a palindrome.

Algorithm: 
since we need to constantly checking if the prefix and suffix of a word is a palindrome, 
we can store all the valid prefix of a word in a dictionary and all the valid suffix in a dictionary.
Time complexity is O(N*k*k) where N is the number of words, k is the length of the longest word
"""
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        reversed_word = collections.defaultdict(int)
        for idx, word in enumerate(words):
            reversed_word[word[::-1]] = idx
        
        res = []
        for idx, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix, suffix = word[:j], word[j:]
                if prefix in reversed_word and reversed_word[prefix] != idx and suffix == suffix[::-1]:
                    res.append([idx, reversed_word[prefix]])
                if j > 0 and suffix in reversed_word and reversed_word[suffix] != idx and prefix == prefix[::-1]:   # 必须check j > 0不然当"ab", "ba"的例子中会有重复的输出
                    res.append([reversed_word[suffix], idx])
        return res
        
Follow up: 也许可以用trie来做
