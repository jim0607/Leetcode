819. Most Common Word

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

Example:

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.


"""
String processing in pipline:
step 1: pre-process: convert all letters in lower case and 
replace the punctuations with spaces cuz they are not valid words
step 2: count the freq of the words that are not banned
isalnum() function in Python programming language checks whether all the characters in a given string is alphanumeric or not.
Alphanumeric:A character that is either a letter or a number
"""
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # step 1: convert all letters in lower case
        # and replace the punctuations with spaces cuz they are not valid words
        words = "".join([word.lower() if word.isalnum() else " " for word in paragraph])
        words = words.split()   # string.split(char) returns a list of string seperated by char
                                # If is not provided then any white space is a separator.
        # step 2: count the freq of the words that are not banned
        banned = set(banned)   # convert list to set so it's faster to search
        counter = collections.Counter(words)
        max_cnt, res = 0, ""
        for word, cnt in counter.items():
            if cnt > max_cnt and word not in banned:
                max_cnt = cnt
                res = word
        return res
