""""
809. Expressive Words

Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  
In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications 
of the following extension operation: choose a group consisting of characters c, 
and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", 
but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  
If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

Example:
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.

Constraints:
0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters
"""


"""
pre-calculate how many successive same chars are there at each idx: "heeellooo" --> {0: 1, 1: 3, 2: 2, 3: 1, 4: 2, 5: 1, 6: 3, 7: 2, 8: 1}
"""
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        # pre-calculate how many successive same chars are there at each idx
        # "heeellooo" --> {0: 1, 1: 3, 2: 2, 3: 1, 4: 2, 5: 1, 6: 3, 7: 2, 8: 1}
        mapping = collections.defaultdict(int)
        mapping[len(s)-1] = 1
        cnt = 1
        for i in range(len(s) - 2, -1, -1):
            if s[i] == s[i+1]:
                cnt += 1
            else:
                cnt = 1
            mapping[i] = cnt

        res = 0
        for word in words:
            if self._is_valid(s, mapping, word):
                res += 1
        return res
    
    def _is_valid(self, s, mapping_s, word):
        """
        Return if s is a valid expressive word for word.
        """
        mapping_word = collections.defaultdict(int)
        mapping_word[len(word)-1] = 1
        cnt = 1
        for i in range(len(word) - 2, -1, -1):
            if word[i] == word[i+1]:
                cnt += 1
            else:
                cnt = 1
            mapping_word[i] = cnt
            
        i, j = 0, 0
        found = False
        while i < len(s) and j < len(word):
            if s[i] != word[j]:
                return False
            if mapping_s[i] < mapping_word[j]:
                return False
            elif mapping_s[i] == mapping_word[j]:
                i += mapping_s[i]
                j += mapping_word[j]
            elif mapping_s[i] >= 3:
                found = True
                i += mapping_s[i]
                j += mapping_word[j]
            else:
                return False
        return i == len(s) and j == len(word) and found
